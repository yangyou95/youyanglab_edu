from django import forms
from django.contrib.auth.forms import UserCreationForm
from webapp.models import User
from captcha.fields import CaptchaField


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length = 60, help_text="请输入邮箱地址")
    captcha = CaptchaField()
    class Meta:
        model = User
        fields = ("email","password1","password2")