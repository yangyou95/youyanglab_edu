from django import forms
from django.contrib.auth.forms import UserCreationForm
from webapp.models import User
from captcha.fields import CaptchaField
from django.contrib.auth import authenticate


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length = 60, help_text="请输入邮箱地址")
    captcha = CaptchaField()
    class Meta:
        model = User
        fields = ("email","password1","password2")

class UserLoginForm(forms.Form):
    email = forms.EmailField(max_length=60, help_text="请输入邮箱地址")
    password = forms.CharField(widget=forms.PasswordInput)
    def clean(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')

        if email and password:
            user = authenticate(email=email, password=password)
            if not user or not user.check_password(password):
                raise forms.ValidationError('用户名或密码输入错误')
        return super(UserLoginForm, self).clean(*args, **kwargs)