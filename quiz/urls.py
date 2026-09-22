from django.urls import path

from . import views

app_name = "quiz"

urlpatterns = [
    path("", views.quiz_list, name="list"),
    path("quiz/<slug:slug>/", views.quiz_detail, name="detail"),
    path("quiz/<slug:slug>/submit/", views.submit_quiz, name="submit"),
    path("results/<int:pk>/", views.result, name="result"),
]
