from django import forms
from django.core.exceptions import ValidationError


class GameForm(forms.Form):
    min_value = forms.IntegerField(widget=forms.NumberInput, label='Левая граница диапазона')
    max_value = forms.IntegerField(widget=forms.NumberInput, label='Правая граница диапазона')
    def clean(self):
        min_value = self.cleaned_data.get('min_value')
        max_value = self.cleaned_data.get('max_value')
        if min_value >= max_value:
            raise ValidationError('Проверьте указанный вами диапазон')
        return super().clean()

class Player2Form(forms.Form):
    attempt = forms.IntegerField(widget=forms.NumberInput, label='Ваше предположение')