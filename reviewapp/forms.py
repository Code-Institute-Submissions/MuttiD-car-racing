from .models import CarCommentModel, Contact
from django import forms


class CommentForm(forms.ModelForm):
    """
    Add a form based on the CarComment model
    """
    class Meta:
        model = CarCommentModel
        fields = (
            'body',)


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'email', 'subject', 'message')
