from django import forms

class SignUp(forms.Form):
    nombre = forms.CharField(label='Nombre de usuario:', required=True)
    email = forms.EmailField(label='e-mail: ', required=True)
    password = forms.CharField(label='Contraseña:', widget=forms.PasswordInput, required=True)
