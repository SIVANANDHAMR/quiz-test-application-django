from django.contrib import admin

from .models import Attempt, Choice, Question, Quiz


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 4


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ("text", "quiz", "order")
    list_filter = ("quiz",)
    inlines = (ChoiceInline,)


@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ("title", "duration_minutes", "is_published", "created_at")
    list_filter = ("is_published",)
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ("title", "description")


@admin.register(Attempt)
class AttemptAdmin(admin.ModelAdmin):
    list_display = ("participant_name", "quiz", "score", "total_questions", "percentage")
    list_filter = ("quiz",)
    search_fields = ("participant_name", "quiz__title")
    readonly_fields = ("started_at", "completed_at")
