from django.db import transaction
from django.shortcuts import get_object_or_404, redirect, render

from .forms import QuizSubmissionForm
from .models import Attempt, Quiz


def _quiz_context(quiz, form):
    questions = quiz.questions.all()
    return {
        "quiz": quiz,
        "form": form,
        "question_fields": [
            (question, form[f"question_{question.pk}"]) for question in questions
        ],
    }


def quiz_list(request):
    quizzes = Quiz.objects.filter(is_published=True).prefetch_related("questions")
    return render(request, "quiz/quiz_list.html", {"quizzes": quizzes})


def quiz_detail(request, slug):
    quiz = get_object_or_404(
        Quiz.objects.prefetch_related("questions__choices"),
        slug=slug,
        is_published=True,
    )
    return render(request, "quiz/quiz_detail.html", _quiz_context(quiz, QuizSubmissionForm(quiz)))


@transaction.atomic
def submit_quiz(request, slug):
    quiz = get_object_or_404(
        Quiz.objects.prefetch_related("questions__choices"),
        slug=slug,
        is_published=True,
    )
    if request.method != "POST":
        return redirect(quiz.get_absolute_url())

    form = QuizSubmissionForm(quiz, request.POST)
    if not form.is_valid():
        return render(
            request,
            "quiz/quiz_detail.html",
            _quiz_context(quiz, form),
            status=400,
        )

    questions = list(quiz.questions.all())
    score = sum(
        form.cleaned_data[f"question_{question.pk}"].is_correct for question in questions
    )
    attempt = Attempt.objects.create(
        quiz=quiz,
        participant_name=form.cleaned_data["participant_name"],
        score=score,
        total_questions=len(questions),
    )
    return redirect("quiz:result", pk=attempt.pk)


def result(request, pk):
    attempt = get_object_or_404(Attempt.objects.select_related("quiz"), pk=pk)
    return render(request, "quiz/result.html", {"attempt": attempt})
