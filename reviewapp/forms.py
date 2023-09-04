from .models import CarCommentModel
from django import forms


class CommentForm(forms.ModelForm):
    """
    Add a form based on the CarComment model
    """
    class Meta:
        model = CarCommentModel
        fields = (
            'body',)
