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


class ContactForm(forms.Form):
    """
    Add a form to contact us page
    """
    name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    message = forms.CharField(widget=forms.Textarea)
