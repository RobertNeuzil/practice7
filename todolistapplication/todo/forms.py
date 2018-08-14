from django import forms

class todoform(forms.Form):
	todotext = forms.Charfield(max_length=40)