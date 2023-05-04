from .models import CarComment
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = CarComment
        fields = ('body',)
