# news/forms.py
from django import forms
from django.forms import ModelForm
from .models import NewsStory

class StoryForm(ModelForm):
    class Meta:
        model = NewsStory
        fields = ['title','pub_date', 'content', 'image_url']
        labels = {
            'title': 'Your Article Title',
            'pub_date': 'Publication date',
            'content': 'The Text Of The Article',
            'image_url': 'Image URL'
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'pub_date': forms.DateInput(
                format='%d/%m/%Y',
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Select a date',
                    'type': 'date'
                    }
                ),
            'content': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': 5
                    }
                ),
            'image_url': forms.URLInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter the image URL'
                    }
                )
        }
    
