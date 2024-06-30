from django import forms
from .models import Question, AnswerChoice


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['text']


class AnswerForm(forms.Form):
    def __init__(self, *args, **kwargs):
        questions = kwargs.pop('questions')
        super(AnswerForm, self).__init__(*args, **kwargs)
        for question in questions:
            choices = [(choice.id, choice.text) for choice in question.answerchoice_set.all()]
            self.fields[f'question_{question.id}'] = forms.ChoiceField(choices=choices, widget=forms.RadioSelect,
                                                                       label=question.text)
