from django import forms

class NewQuoteForm(forms.Form):
    email = forms.EmailField()
    body = forms.CharField(max_length=2000, widget=forms.Textarea)
