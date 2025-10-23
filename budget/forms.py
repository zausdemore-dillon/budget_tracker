from django import forms
from .models import Entries

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entries
        fields = ['date', 'item','amount','ttype']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'amount': forms.NumberInput(attrs={'step': '0.01', 'min': '0'}),
        }
