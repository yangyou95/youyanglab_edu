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
    active = models.BooleanField(default = False)
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


# 课程模型
class Course(models.Model):
    """章节"""
    course_name = models.CharField(max_length = 200)
    # 之后可以加图片

    def __str__(self):
        return self.course_name

# 章节模型
class Chapter(models.Model):
    """章节"""
    course = models.ForeignKey(Course, on_delete = models.CASCADE)
    chapter_name = models.CharField(max_length = 200)
    # 之后可以加图片

    def __str__(self):
        return self.chapter_name



# 课程模型
class Lesson(models.Model):
    """课程名字及视频"""
    chapter = models.ForeignKey(Chapter, on_delete = models.CASCADE)
    lesson_name = models.CharField(max_length = 200)
    video_url = models.CharField(max_length = 300)
    created_date = models.DateTimeField('Created date')

    def __str__(self):
        return self.lesson_name

    def get_next(self):
        chapter_id = self.chapter.id
        next = Lesson.objects.filter(chapter_id=chapter_id,id__gt=self.id).order_by('id').first()
        if next:
            return next
        # If the current card is the last one, return the first card in the deck
        else:
            return Lesson.objects.all().order_by('id').first()

    def get_chapter_all_lessons(self):
        chapter_id = self.chapter.id
        all_lessons_list = Lesson.objects.filter(chapter_id=chapter_id)
        return all_lessons_list


# 存储问题的模型
class ClassQuestion(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete = models.CASCADE, null=True)
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


