from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404
# from django.template import loader
from django.urls import reverse
from django.views import generic
from django.contrib.auth import login as auth_login, authenticate
from webapp.forms import RegistrationForm
# Create your views here.
from .models import *

# 提取问题并显示在前端

#改良前
# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     context = {'latest_question_list': latest_question_list}
#     context['variable'] = "传递参数测试"
#     return render(request, 'webapp/index.html', context)

#     # # 定义的模板
#     # template = loader.get_template('webapp/index.html')
#     # context = {
#     #     'latest_question_list':latest_question_list,
#     # }
#     # return HttpResponse(template.render(context, request))

# def detail(request, question_id):
#     try:
#         question = Question.objects.get(pk=question_id)
#     except Question.DoesNotExist:
#         raise Http404("Question does not exist")
#     return render(request, 'webapp/detail.html', {'question': question})

# def results(request, question_id):
#     # response = "You're looking at the results of question %s."
#     # return HttpResponse(response % question_id)
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'webapp/results.html', {'question': question})


# def index(request):
#     # latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     # context = {'latest_question_list': latest_question_list}
#     # context['variable'] = "传递参数测试"
#     # return render(request, 'webapp/index.html', context)
#
#     return render(request, 'webapp/index.html')


class index(generic.ListView):
    template_name = 'webapp/index.html'
    context_object_name = 'all_courses'

    def get_queryset(self):
        return Course.objects.all()

# class course(generic.ListView):
#     template_name = 'webapp/course.html'
#     context_object_name = 'question_test_list'
#
#     def get_queryset(self):
#         """Return the last five published questions."""
#         return ClassQuestion.objects.all()

class course(generic.DetailView):
    template_name = 'webapp/course.html'
    model = Course


#def detailpage(request):
#   return render(request, 'webapp/detailpage.html')

class detailpage(generic.DetailView):
    template_name = 'webapp/detailpage.html'
    model = Lesson

    # def get_context_data(self, **kwargs):
    #     try:
    #         ret = Lesson.objects.filter(id__gt=curr_id).order_by("id")[0:1].get().id
    #     except Image.DoesNotExist:
    #         ret = Lesson.objects.aggregate(Min("id"))['id__min']
    #     return ret


    #def get_queryset(self):
     #   """Return the last five published questions."""
      #  return ClassQuestion.objects.all()




# def registerView(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('login_url')
#     else:
#         form = UserCreationForm()
#     return render(request, 'webapp/register.html',{'form':form})

def registration_view(request):
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=raw_password)
            auth_login(request, account)
            return redirect('/webapp')
        else:
            context['registration_form'] = form
    else:
        form = RegistrationForm()
        context['registration_form'] = form
    return render(request, 'webapp/register.html',context)

def userpage(request):
    return render(request, 'webapp/usr.html')

def login(request):
    return render(request, 'webapp/login.html')

def signup(request):
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=raw_password)
            auth_login(request, account)
            return redirect('/')
        else:
            context['registration_form'] = form
    else:
        form = RegistrationForm()
        context['registration_form'] = form
    return render(request, 'webapp/signup.html',context)

def signin(request):
    return render(request, 'webapp/signin.html')

def forget(request):
    return render(request, 'webapp/forget.html')

#改良后
# class IndexView(generic.ListView):
#     template_name = 'webapp/index.html'
#     # context_object_name = 'latest_question_list'

class QuestionsView(generic.ListView):
    template_name = 'webapp/questions.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'webapp/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'webapp/results.html'

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'webapp/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('webapp:results', args=(question.id,)))

# Testcontent模型的显示
def showtestcontent(request):
    contents_list = Testcontent.objects.order_by('-created_date')[:5]
    # context = {'latest_question_list': latest_question_list}
    # context['variable'] = "传递参数测试"
    # return render(request, 'webapp/index.html', context)

    return render(request, 'webapp/showtestcontent.html',{'contents_list':contents_list})

#test

class QuestionTest(generic.ListView):
    template_name = 'webapp/questiontest.html'
    context_object_name = 'question_test_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return ClassQuestion.objects.all()

class ChoiceTest(generic.DetailView):
    model = ClassQuestion
    template_name = 'webapp/choicetest.html'

# 课程分类页面
def Class(request):
    return render(request, 'webapp/class.html')

def ClassDetail(request):
    return render(request, 'webapp/classdetail.html')


