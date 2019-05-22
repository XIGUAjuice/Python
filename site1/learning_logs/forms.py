from django import forms
from .models import Topic
from .models import Content


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''}


class ContentForm(forms.ModelForm):
    class Meta:
        model = Content
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80}), 'date_add': forms.Textarea(attrs=({'cols': 80}))}
