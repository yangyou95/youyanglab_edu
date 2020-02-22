from django.db import models
# from DjangoUeditor.models import UeditorField
from django.utils import timezone
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)



# # My own users
# class

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