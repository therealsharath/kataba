from rest_framework.generics import ListAPIView

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

class AnswerListView(ListAPIView):
    questions = []
    for question in Question.objects.filter(confidence_score=0):
        questions.append(question.user_question)
    
    if questions != []:
        sample_speech = speech.sample_recognize("gs://cloud-samples-tests/speech/brooklyn.flac")
        print(sample_speech)
        
        answers = answer.predict(sample_speech, questions)
        for question, answer in zip(questions, answers):
            to_change = Question.objects.filter(user_question=question)[0]
            to_change.model_answer=answer
            to_change.save()

    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

