from django.contrib import admin

# Register your models here.
from .models import Question, Choice, Introduction

admin.site.site_header = "优扬实验室管理后台"
admin.site.site_title = "优扬实验室后台"

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields':['introduction']}),
    (None, {'fields':['question_text']}),
    ('创建时间', {'fields': ['pub_date'], 'classes':['collapse']}),]
    inlines = [ChoiceInline]

# admin.site.register(Question)
# admin.site.register(Choice)

admin.site.register(Question, QuestionAdmin)
admin.site.register(Introduction)