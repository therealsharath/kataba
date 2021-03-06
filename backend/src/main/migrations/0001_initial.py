# Generated by Django 3.1 on 2020-08-15 01:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lecture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lecture_id', models.CharField(max_length=9)),
                ('lecture_url', models.TextField()),
                ('lecture_text', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lecture_id', models.CharField(max_length=9)),
                ('user_question', models.TextField()),
                ('model_answer', models.TextField(blank=True, null=True)),
                ('confidence_score', models.IntegerField(blank=True, null=True)),
                ('answered', models.BooleanField(default=False)),
            ],
        ),
    ]
