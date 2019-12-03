from django.shortcuts import render

# Create your views here.
from .models import Question, Choice

# 提取问题并显示在前端
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    context['variable'] = "传递参数测试"
    return render(request, 'webapp/index.html', context)