from django.db import models


class Question(models.Model):
    user_question = models.TextField()
    model_answer = models.CharField(max_length=200)
    confidence_score = models.IntegerField()

    def __str__(self):
        return 'Question: ' + self.user_question + '\n Answer: ' + self.model_answer


class Lecture(models.Model):
    lecture_text = models.TextField()

    def __str__(self):
        return self.lecture_text
