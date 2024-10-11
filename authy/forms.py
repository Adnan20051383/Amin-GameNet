# forms.py

from django import forms
from .models import Reserve


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reserve
        fields = ['reserver', 'players_num']
        widgets = {
            'reserver': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Enter name',
                'required': True
            }),
            'players_num': forms.NumberInput(attrs={
                'class': 'form-input',
                'value': '1',
                'min': 1,
                'max': 6,
                'required': True
            }),
        }
        labels = {
            'reserver': 'Your Name',
            'players_num': 'Number of Players',
        }