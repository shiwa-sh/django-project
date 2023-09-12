from django import forms
from .models import Comments

class CommestForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('comment', 'author')