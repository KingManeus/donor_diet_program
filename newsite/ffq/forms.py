from django import forms
from .models import Identify, Question, Choice

class IForm(forms.ModelForm):
    class Meta:
        model = Identify
        fields = ['iNumber','iNumberRepeat']
        
class TestChoice(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['question_text']

    
    