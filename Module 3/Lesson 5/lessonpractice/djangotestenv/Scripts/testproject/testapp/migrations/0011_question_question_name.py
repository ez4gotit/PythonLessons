# Generated by Django 5.0.6 on 2024-07-02 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0010_superquestion_question_level'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='question_name',
            field=models.CharField(default='Вопрос', max_length=20),
        ),
    ]
