from django import forms

class LoginForm(forms.Form):
    phone = forms.CharField(label="شماره تلفن", max_length=20)
    password = forms.CharField(label="پسورد", widget=forms.PasswordInput)
