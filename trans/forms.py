from django import forms


class MyForm(forms.Form):
    button_value = forms.CharField()