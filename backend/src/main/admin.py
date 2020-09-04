from django.contrib import admin

from .models import Lecture, Question

admin.site.register(Lecture)
admin.site.register(Question)