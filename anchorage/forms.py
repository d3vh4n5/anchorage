from django import forms
from django.core import validators
from django.forms import ValidationError

def largo_validate(value):
    print(value)
    if len(value) >10 or len(value)< 8:
        raise ValidationError("Debe tener entre 8 y 10 caracteres", code="error_largo",)

class SignUp(forms.Form):
    SEX_CHOICES = (
        (1, "Masculino"),
        (2, "Femenino"),
        (3, "Otro.."),
    )

    nombre = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label='Nombre de usuario:', required=True)
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}), label='e-mail: ', required=True)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), label='Contraseña:', required=True, validators=(largo_validate, ))
    sexo = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-select'}),label='Sexo: ', choices=SEX_CHOICES)
    nacimiento = forms.DateField(
        label='Fecha de nacimiento:',
        widget=forms.SelectDateWidget(
            years=range(1920, 2023),
            attrs={'class': 'form-select'}
        )
    )
    terms = forms.BooleanField(
        label='He leído y acepto los términos de uso ', 
        required=True, 
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )

class Login(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control mt-2 mb-2'}), required=True)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control mt-2 mb-2'}), label='Contraseña:', required=True, validators=(largo_validate, ))
    noRobot = forms.BooleanField(
        label='No soy un robot.', 
        required=True, 
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input mt-2 mb-2'})
    )
