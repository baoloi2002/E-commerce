from django import forms
from django.contrib.auth.forms import UserCreationForm
from userauths.models import User


class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={"placeholder": "Username", "class": "form-control"}
        )
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={"placeholder": "Email", "class": "form-control"})
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"placeholder": "Password", "class": "form-control"}
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"placeholder": "Confirm Password", "class": "form-control"}
        )
    )

    class Meta:
        model = User
        fields = ["email", "username", "password1", "password2"]
        labels = {
            "email": "Email",
            "username": "Username",
            "password1": "Password",
            "password2": "Confirm Password",
        }
        help_texts = {
            "email": "Enter your email address",
            "username": "Enter your username",
            "password1": "Enter your password",
            "password2": "Confirm your password",
        }
        widgets = {
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "username": forms.TextInput(attrs={"class": "form-control"}),
            "password1": forms.PasswordInput(attrs={"class": "form-control"}),
            "password2": forms.PasswordInput(attrs={"class": "form-control"}),
        }
