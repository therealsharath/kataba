from django.urls import path, include

from .views import QuestionListView, LectureListView, QuestionCreateView, QuestionDetailView,LectureCreateView, answer_question

urlpatterns = [
    path('', QuestionListView.as_view()),
    path('lectures/', LectureListView.as_view()),
    path('<pk>', QuestionDetailView),
    path('create/', QuestionCreateView.as_view()),
    path('create-lecture/', LectureCreateView.as_view()),
    path('answer/', answer_question),
]
