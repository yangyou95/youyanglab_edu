from django.urls import path
from .import views

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
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
