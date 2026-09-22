from django.core.management.base import BaseCommand

from quiz.models import Choice, Question, Quiz


class Command(BaseCommand):
    help = "Create a sample published Django quiz."

    questions = [
        (
            "Which Django file typically defines URL routes?",
            [
                ("models.py", False),
                ("urls.py", True),
                ("admin.py", False),
                ("forms.py", False),
            ],
        ),
        (
            "Which command applies database migrations?",
            [
                ("python manage.py migrate", True),
                ("python manage.py serve", False),
                ("python manage.py routes", False),
                ("python manage.py deploy", False),
            ],
        ),
        (
            "Which Django component is responsible for data structure definitions?",
            [
                ("Templates", False),
                ("Views", False),
                ("Models", True),
                ("Middleware", False),
            ],
        ),
        (
            "What does CSRF protection help prevent?",
            [
                ("Broken images", False),
                ("Unauthorized form submissions", True),
                ("Slow database queries", False),
                ("Missing CSS", False),
            ],
        ),
    ]

    def handle(self, *args, **options):
        quiz, _ = Quiz.objects.update_or_create(
            slug="django-foundations",
            defaults={
                "title": "Django Foundations",
                "description": "A quick assessment of the concepts behind a Django web application.",
                "duration_minutes": 5,
                "is_published": True,
            },
        )

        for order, (text, choices) in enumerate(self.questions, start=1):
            question, _ = Question.objects.update_or_create(
                quiz=quiz,
                order=order,
                defaults={"text": text},
            )
            question.choices.all().delete()
            Choice.objects.bulk_create(
                [
                    Choice(question=question, text=choice_text, is_correct=is_correct)
                    for choice_text, is_correct in choices
                ]
            )

        self.stdout.write(self.style.SUCCESS(f"Demo quiz ready: {quiz.get_absolute_url()}"))
