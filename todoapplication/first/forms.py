from django import forms



class ToDoForm(forms.Form):
	text = forms.CharField(max_length=40)