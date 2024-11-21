from django import forms

class textForm(forms.Form):
    input_text = forms.CharField(label="Enter the text to summarize", widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'id_input_text'}))
