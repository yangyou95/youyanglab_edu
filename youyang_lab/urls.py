"""youyang_lab URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', include('webapp.urls')),
    path('admin/', admin.site.urls),
    path('captcha/', include('captcha.urls')),   # 增加这一行, 验证码

    # 忘记重置密码 分为四步
    # 1. 发送邮件页面 rest_password template_name="webapp/forget.html"
    # 2. 发送邮件成功页面，让用户去确认 PassWordRestDone
    # 3. 邮件内容页面（邮件点击链接页面）
    # 4. 密码重置页面 PassWordResetConfirm
    # 5. 密码成功更改页面
    path('reset_password/',
         auth_views.PasswordResetView.as_view(template_name='webapp/forget.html'),
         name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),
    path('rest_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),
]
