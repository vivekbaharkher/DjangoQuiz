# Generated by Django 5.0.3 on 2024-03-29 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizapp', '0004_alter_profile_score_alter_profile_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='played',
            field=models.BooleanField(default=False),
        ),
    ]
