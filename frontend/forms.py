from django import forms
from question.models import question
from answer.models import answer

class askquestion_form(forms.ModelForm):
    class Meta:
        model=question
        fields=['category','question','date']

class answer_form(forms.ModelForm):
    class Meta:
        model=answer
        fields=['answer', 'image', 'date']
