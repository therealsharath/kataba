from django.db import models

# Create your models here.
class Lecture(models.Model):
    lecture_id = models.CharField(max_length=9)
    lecture_url = models.TextField()
    lecture_text = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.lecture_id

class Question(models.Model):
    lecture_id = models.CharField(max_length=9)
    user_question = models.TextField()
    model_answer = models.TextField(blank=True, null=True)
    confidence_score = models.IntegerField(blank=True, null=True)
    answered = models.BooleanField(default=False)

    def __str__(self):
        return self.lecture_id