from django import forms

class QuoteForm(forms.Form):
    quote = forms.CharField(label='Quote', max_length=3000)
    person = forms.CharField(label='Person', max_length=500)