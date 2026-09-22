from django import forms

from .models import Quiz


class QuizSubmissionForm(forms.Form):
    participant_name = forms.CharField(
        label="Your name",
        max_length=100,
        widget=forms.TextInput(attrs={"placeholder": "Enter your name"}),
    )

    def __init__(self, quiz: Quiz, *args, **kwargs):
        super().__init__(*args, **kwargs)
        questions = quiz.questions.prefetch_related("choices").all()
        for question in questions:
            self.fields[f"question_{question.pk}"] = forms.ModelChoiceField(
                queryset=question.choices.all(),
                widget=forms.RadioSelect,
                required=True,
                label=question.text,
                empty_label=None,
            )
