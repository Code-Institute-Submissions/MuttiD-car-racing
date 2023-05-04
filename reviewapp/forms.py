from .models import CarComment
from django import forms


class CommentForm(forms.ModelForm):
    """
    Add a form based on the Post model
    """
    class Meta:
        model = CarComment
        fields = ('body',)
