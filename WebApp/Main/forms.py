from django import forms

class ConvertLink(forms.Form):
    name = forms.CharField(label="Enter Link", max_length=200)
