# Generated by Django 5.0.6 on 2024-06-27 17:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0008_alter_choice_votes'),
    ]

    operations = [
        migrations.CreateModel(
            name='SuperQuestion',
            fields=[
                ('question_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='testapp.question')),
            ],
            bases=('testapp.question',),
        ),
    ]
