from django.contrib import admin
from django.contrib.auth import get_user_model
# Register your models here.
from .models import*


User = get_user_model()
admin.site.site_header = "优扬实验室管理后台"
admin.site.site_title = "优扬实验室后台"


class UserAdmin(admin.ModelAdmin):
    search_field = ['email']
    class Meta:
        model = User

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields':['introduction']}),
    (None, {'fields':['question_text']}),
    ('创建时间', {'fields': ['pub_date'], 'classes':['collapse']}),]
    inlines = [ChoiceInline]

class ClassChoiceInline(admin.TabularInline):
    model = ClassQuestionChoice
    extra = 3

class ClassQuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None,{'fields':['lesson']}),
        (None, {'fields':['question_text']}),]
    inlines = [ClassChoiceInline]


class Lessons(admin.ModelAdmin):
    fieldsets = [('所属章节',{'fields':['chapter']}),
                 ('课程小节名称',{'fields':['lesson_name']}),
                 ('课程小节Markdown文件',{'fields':['file']}),
                 ('课程小节视频链接',{'fields':['video_url']}),
                 ('创建时间', {'fields': ['created_date']}),]


class Chapters(admin.ModelAdmin):
    fieldsets = [('所属课程',{'fields':['course']}),
                 ('章节名称',{'fields':['chapter_name']}),]


# admin.site.register(Question)
# admin.site.register(Choice)

admin.site.register(User, UserAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Introduction)
admin.site.register(Testcontent)

# 选择题->课程小节->章节->课程
admin.site.register(ClassQuestion, ClassQuestionAdmin)
admin.site.register(Lesson, Lessons)
admin.site.register(Chapter, Chapters)
admin.site.register(Course)


# admin.site.register(ClassQuestion)
# admin.site.register(ClassQuestionChoice)