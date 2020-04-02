from django import forms
from .models import Review, Car

from ckeditor.widgets import CKEditorWidget



class ReviewAdminForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Review
        fields = ['car', 'title', 'text']
