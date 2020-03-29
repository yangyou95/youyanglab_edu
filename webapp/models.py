from django.db import models
# from DjangoUeditor.models import UeditorField
from django.utils import timezone
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, is_active = True, is_staff = False, is_admin = False):
        if not email:
            raise ValueError("用户注册必须输入邮箱")
        if not password:
            raise ValueError("用户注册必须输入密码")
        user_obj = self.model(
            email = self.normalize_email(email)
        )
        user_obj.set_password(password)
        user_obj.staff = is_staff
        user_obj.admin = is_admin
        user_obj.active = is_active
        # user_obj.timestamp = timezone.get_current_timezone_name()
        user_obj.save(using=self._db)
        return user_obj

    def create_staffuser(self, email, password=None):
        user = self.create_user(
            email,
            password = password,
            is_staff=True,
        )
        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(
            email,
            password = password,
            is_staff = True,
            is_admin = True,
        )
        return user


# # My own users
class User(AbstractBaseUser):
    email = models.EmailField(max_length=255, unique=True)
    active = models.BooleanField(default = True)
    staff = models.BooleanField(default = False)
    admin = models.BooleanField(default = False)
    # timestamp = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD ='email'
    REQUIRED_FIELD = []

    objects = UserManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True


    @property
    def is_staff(self):
        return self.staff

    @property
    def is_active(self):
        return self.active

    @property
    def is_admin(self):
        return self.admin

# 建立一个个人资料模型，和用户User一一对应
# class Profile(models.Model):
#     user = models.OneToOneField(User)
#
#

# Create your models here.
class Introduction(models.Model):
    #Premier key
    intro_text = models.CharField(max_length=1000, blank = True)
    created_date = models.DateTimeField('Created date')

    def __str__(self):
        return self.intro_text

class Question(models.Model):
    # Foreignkey link to the premier key of this table
    introduction = models.ForeignKey(Introduction, on_delete = models.CASCADE)
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    # Foreignkey link to the premier key of this table
    question = models.ForeignKey(Question, on_delete = models.CASCADE)
    choice_text = models.CharField(max_length = 200)
    votes = models.IntegerField(default = 0)

    def __str__(self):
        return self.choice_text


# 存储一段文字的模型
class Testcontent(models.Model):
    content = models.CharField(max_length = 300)
    created_date = models.DateTimeField('Created date')

    # def __str__(self):
    #     return self.content

# 存储问题的模型
class ClassQuestion(models.Model):
    question_text = models.CharField(max_length=200)

    def __str__(self):
        return self.question_text

# 存储选项的模型
class ClassQuestionChoice(models.Model):
    question = models.ForeignKey(ClassQuestion, on_delete = models.CASCADE)
    choice_text = models.CharField(max_length = 200)
    answer = models.BooleanField(default = False)
    order_in_list = models.IntegerField(default=1)


    def __str__(self):
        return self.choice_text