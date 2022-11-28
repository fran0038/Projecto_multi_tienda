from django import forms

class Formulario(forms.Form):

    nombre = forms.CharField()
    apellido =forms.CharField()
    telefono = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())

class Web(forms.Form):
    email = forms.EmailField()
    password = forms.CharField()