from django.contrib import admin
from .models import Test, Question, AnswerChoice, UserResponse

admin.site.register(Test)
admin.site.register(Question)
admin.site.register(AnswerChoice)
admin.site.register(UserResponse)
