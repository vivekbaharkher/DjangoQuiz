from django.contrib import admin
from .models import Quiz
from .models import Question
from .models import Choice
from .models import Profile

# Register your models here.
admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Profile)