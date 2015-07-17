from django.contrib import admin

from .models import Question, Choice, Identify



class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2

class QuestionAdmin(admin.ModelAdmin):
    model = Question
    extra = 1
    inlines = [ChoiceInline]
    
admin.site.register(Question,QuestionAdmin)
admin.site.register(Identify)
