from django.urls import path, include

from .views import QuestionListView, LectureListView, AnswerListView, QuestionCreateView, QuestionDetailView

urlpatterns = [
    path('', QuestionListView.as_view()),
    path('lectures/', LectureListView.as_view()),
    path('answers/', AnswerListView.as_view()),
    path('<pk>', QuestionDetailView),
    path('create/', QuestionCreateView.as_view()),
]
