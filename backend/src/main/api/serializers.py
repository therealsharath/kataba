from rest_framework import serializers
from main.models import Question, Lecture


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('user_question', 'model_answer', 'confidence_score')


class LectureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lecture
        fields = '__all__'
