from rest_framework.generics import ListAPIView

from main.models import Question, Lecture
from .serializers import QuestionSerializer, LectureSerializer
from . import answer

class QuestionListView(ListAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class LectureListView(ListAPIView):
    queryset = Lecture.objects.all()
    serializer_class = LectureSerializer

class AnswerListView(ListAPIView):
    questions = []
    print(Question.objects.filter(confidence_score=1))
    for question in Question.objects.filter(confidence_score=1):
        questions.append(question.user_question)
    
    answers = answer.predict(
        """🤗 Magnesia and magnesium ribbon is heated. 
        It starts burning or undergoes combustion engine revving bonds. 
        It combines with oxygen to form magnesium oxide and liberals heat and light.""", questions
    )

    result = []
    for question, answer in zip(questions, answers):
        to_change = Question.objects.filter(user_question=question)[0]
        to_change.model_answer=answer
        to_change.save()
        result.append((question, answer))

    print(result)
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

