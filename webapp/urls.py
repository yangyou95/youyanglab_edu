from django.urls import path
from .import views
from django.contrib.auth.views import LoginView

# 在每个应用里，规定命名空间app_name，防止其他应用里也有同名的视图
app_name = 'webapp'
urlpatterns = [
    # 改良前

    # path('', views.index, name = 'index'),
    #  # ex: /webapp/5/
    # path('<int:question_id>/', views.detail, name='detail'),
    # # ex: /webapp/5/results/
    # path('<int:question_id>/results/', views.results, name='results'),
    # # ex: /webapp/5/vote/
    # path('<int:question_id>/vote/', views.vote, name='vote'),

    #改良后
    path('', views.index.as_view(), name='index'),
    path('course/<int:pk>/', views.course.as_view(), name='course'),
    path('lesson/<int:pk>/',views.detailpage.as_view(), name = 'detailpage'),
    path('questions/', views.QuestionsView.as_view(), name='questions'),
    path('questions/<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('questions/<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('questions/<int:question_id>/vote/', views.vote, name='vote'),
    path('testcontent/', views.showtestcontent, name = 'showtestcontent'),

#     注册登录
    path('register/',views.registration_view, name = "register_url"),
    path('login/',LoginView.as_view(), name = "login_url" ),
    path('userpage/',views.userpage, name = "user_url"),
    path('signin/',views.signin, name = "signin"),
    path('signup/',views.signup, name = 'signup'),
    path('forget/',views.forget, name='forget'),


    #test questions
    path('questiontest/', views.QuestionTest.as_view(), name = "question_test"),
    path('questiontest/<int:pk>/', views.ChoiceTest.as_view(), name='choice_test'),

    # 课程分类页面
    path('class/', views.Class, name = 'class'),
    path('classdetail/', views.ClassDetail, name = 'classdetail'),
]

