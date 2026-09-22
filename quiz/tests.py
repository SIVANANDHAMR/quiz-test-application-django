from django.test import TestCase
from django.urls import reverse

from .models import Attempt, Choice, Question, Quiz


class QuizFlowTests(TestCase):
    def setUp(self):
        self.quiz = Quiz.objects.create(
            title="Python Basics",
            slug="python-basics",
            description="A test quiz.",
            duration_minutes=5,
            is_published=True,
        )
        self.questions = []
        for order, text in enumerate(("What is Django?", "Which keyword defines a function?"), start=1):
            question = Question.objects.create(quiz=self.quiz, text=text, order=order)
            self.questions.append(question)
        self.correct_choices = [
            Choice.objects.create(question=self.questions[0], text="A web framework", is_correct=True),
            Choice.objects.create(question=self.questions[1], text="def", is_correct=True),
        ]
        self.wrong_choices = [
            Choice.objects.create(question=self.questions[0], text="A database", is_correct=False),
            Choice.objects.create(question=self.questions[1], text="classify", is_correct=False),
        ]

    def test_only_published_quizzes_are_listed(self):
        response = self.client.get(reverse("quiz:list"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Python Basics")

    def test_submission_calculates_score_and_redirects_to_result(self):
        response = self.client.post(
            reverse("quiz:submit", kwargs={"slug": self.quiz.slug}),
            {
                "participant_name": "Sivanandham",
                f"question_{self.questions[0].pk}": self.correct_choices[0].pk,
                f"question_{self.questions[1].pk}": self.wrong_choices[1].pk,
            },
        )

        attempt = Attempt.objects.get()
        self.assertRedirects(response, reverse("quiz:result", kwargs={"pk": attempt.pk}))
        self.assertEqual(attempt.score, 1)
        self.assertEqual(attempt.total_questions, 2)
        self.assertEqual(attempt.percentage, 50)

    def test_missing_answer_is_rejected_without_creating_attempt(self):
        response = self.client.post(
            reverse("quiz:submit", kwargs={"slug": self.quiz.slug}),
            {"participant_name": "Sivanandham"},
        )

        self.assertEqual(response.status_code, 400)
        self.assertFalse(Attempt.objects.exists())
