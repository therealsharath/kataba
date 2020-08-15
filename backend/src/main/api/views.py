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

class QuestionDetailView(RetrieveAPIView):
    querry_set  = Question.objects.all()
    serializer_class = QuestionSerializer

class AnswerListView(ListAPIView):
    questions = []
    for question in Question.objects.all():
        questions.append(question.user_question)
    
    if questions != []:
        # sample_speech = speech.sample_recognize("gs://cloud-samples-tests/speech/brooklyn.flac")
        sample_speech = "Independence Day is annually celebrated on 15 August, as a national holiday in India commemorating the nation's independence from the United Kingdom on 15 August 1947, the day when the provisions of the Indian Independence Act 1947, as passed by the United Kingdom Parliament, which transferred legislative sovereignty to the Indian Constituent Assembly came into effect."
        
        answers = answer.predict(sample_speech, questions)
        for question, answer in zip(questions, answers):
            to_change = Question.objects.filter(user_question=question)[0]
            to_change.model_answer=answer
            to_change.save()

    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
