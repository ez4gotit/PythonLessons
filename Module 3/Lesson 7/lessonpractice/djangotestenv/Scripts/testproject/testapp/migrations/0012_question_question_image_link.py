# Generated by Django 5.0.6 on 2024-07-02 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0011_question_question_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='question_image_link',
            field=models.URLField(default='https://media1.tenor.com/m/qfQ2YhGCHhoAAAAC/shrek-dance.gif'),
        ),
    ]
