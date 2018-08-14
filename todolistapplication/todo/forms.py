from django import forms

class Todoform(forms.Form):
	todotext = forms.CharField(max_length=40, widget = forms.TextInput(

		attrs={'class': 'form-control', 'placeholder': 'What do you want to do? :-)', 
		'aria-label':'Todo', 'aria-describedby' : 'add-btn'}


		))