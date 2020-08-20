from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView

from main.models import Question, Lecture
from .serializers import QuestionSerializer, LectureSerializer
from . import answer
from . import speech

class QuestionListView(ListAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class LectureListView(ListAPIView):
    queryset = Lecture.objects.all()
    serializer_class = LectureSerializer

class QuestionCreateView(CreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class LectureCreateView(CreateAPIView):
    queryset = Lecture.objects.all()
    serializer_class = LectureSerializer

class QuestionDetailView(RetrieveAPIView):
    querry_set  = Question.objects.all()
    serializer_class = QuestionSerializer

class AnswerListView(ListAPIView):
    sample_lecture = Lecture.objects.filter(lecture_id="00000000")
    questions = []
    for question in Question.objects.filter(lecture_id="00000000"):
        questions.append(question.user_question)

    if sample_lecture != [] and questions != []:
        lecture_text = sample_lecture[0].lecture_text
        
        answers = answer.predict(lecture_text, questions)
        for question, answer in zip(questions, answers):
            to_change = Question.objects.filter(user_question=question)[0]
            if to_change.answered != True:
                to_change.model_answer=answer
                to_change.answered=True
                to_change.save()
        
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer