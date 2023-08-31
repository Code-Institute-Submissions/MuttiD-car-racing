from django import forms
from .models import CarCommentModel


class CommentForm(forms.ModelForm):
    """
    Add a form based on the CarComment model
    """
    class Meta:
        model = CarCommentModel
        fields = (
            'body',)
