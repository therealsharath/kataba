from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView
from rest_framework.decorators import api_view
from rest_framework.response import Response

from main.models import Question, Lecture
from .serializers import QuestionSerializer, LectureSerializer
from . import answer

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

@api_view(['POST',])
def answer_question(self):
    sample_lecture = Lecture.objects.filter(lecture_id="00000000")[0]
    questions = []
    for question in Question.objects.filter(lecture_id="00000000"):
        if question.answered == False:
            questions.append(question.user_question)

    if sample_lecture != [] and questions != []:
        lecture_text = sample_lecture.lecture_text
        answers = answer.predict(lecture_text, questions)
        for question, model_given_answer in zip(questions, answers):
            to_change = Question.objects.filter(user_question=question)[0]
            if to_change.answered != True:
                if model_given_answer != '':
                    to_change.model_answer=model_given_answer
                else:
                    to_change.model_answer="Lecture has no relevant information"
                to_change.answered=True
                to_change.save()

    data = {}
    data['answered'] = True
    return Response(data)