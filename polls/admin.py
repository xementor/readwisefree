from django.contrib import admin
from .models import Question, Choice, User, Vote

# Register your models here.
admin.site.register(Vote)
admin.site.register(User)
admin.site.register(Question)
admin.site.register(Choice)
