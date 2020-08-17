from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text
from django.template.loader import get_template
from django.urls import reverse
from django.views import generic
from django.contrib.auth import login as auth_login, authenticate, logout
from webapp.forms import RegistrationForm, UserLoginForm
# Create your views here.
from .models import *
from .tokens import user_tokenizer
from django.views import View
from django.contrib import messages
from django.core.mail import EmailMessage, send_mail
import json
from django.conf import settings

# class index(generic.ListView):
#     template_name = 'webapp/index.html'
#     context_object_name = 'all_courses'
#
#     def get_queryset(self):
#         return Course.objects.all()


class course(generic.DetailView):
    template_name = 'webapp/course.html'
    model = Course


#def detailpage(request):
#   return render(request, 'webapp/detailpage.html')

class detailpage(generic.DetailView):
    template_name = 'webapp/detailpage.html'
    model = Lesson


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

# 注册类
class RegisterView(View):
    def get(self, request):
        return render(request, 'webapp/signup.html', {'registration_form': RegistrationForm()})

    def post(self, request):
        context = {}
        if request.POST:
            form = RegistrationForm(request.POST)
            if form.is_valid():
                user = form.save(commit=False)
                user.is_active = False
                user.save()
                token = user_tokenizer.make_token(user)
                user_id = urlsafe_base64_encode(force_bytes(user.id))
                url = 'http://127.0.0.1:8000' + reverse('webapp:confirm_email', kwargs={'user_id': user_id, 'token': token})
                message = get_template('webapp/register_email.html').render({'confirm_url': url})
                mail = EmailMessage('优扬实验室账户邮箱认证', message, to=[user.email], from_email=settings.EMAIL_HOST_USER,headers={'Message-ID': 'foo'})
                mail.content_subtype = 'html'
                mail.send()
                # send_mail('优扬实验室账户邮箱认证', message, settings.EMAIL_HOST_USER,[user.email])
                return render(request, 'webapp/signin.html', {
                    'form': UserLoginForm(),
                    'message': f'一封邮箱认证邮件已发送到 {user.email}. 请确认完成注册后登录'
                })
            else:
                context['registration_form'] = form
                return render(request, 'webapp/signup.html', context)
        else:
            form = RegistrationForm()
            context['registration_form'] = form
        return render(request, 'webapp/signin.html', context)

class ConfirmRegistrationView(View):
    def get(self, request, user_id, token):
        user_id = force_text(urlsafe_base64_decode(user_id))
        user = User.objects.get(pk=user_id)
        context = {
            'form':UserLoginForm(),
            'message':False,
        }
        if user and user_tokenizer.check_token(user, token):
            user.is_active = True
            user.save()
            context['message'] = True
        return render(request, 'webapp/confirmReg.html', context)


# 登录核心程序
def signincore(request):
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        user = authenticate(email=email, password=password)
        auth_login(request, user)
    return form


def signin(request):
    next = request.GET.get('next')
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        user = authenticate(email=email,password=password)
        auth_login(request, user)

        if next:
            return redirect(next)
        return redirect('/')
    context  = {'form':form,}
    return render(request, 'webapp/signin.html',context)

def logout_view(request):
    logout(request)
    return redirect('/')


def forget(request):
    return render(request, 'webapp/forget.html')

def password_sent(request):
    return render(request, 'webapp/passwordsent.html')

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
    all_course = Course.objects.all()
    context = {"form": signincore(request), "all_courses":all_course}
    return render(request, 'webapp/class.html',context)

def ClassDetail(request, class_id):
    class_detail = get_object_or_404(Course, pk=class_id)
    context = {"form": signincore(request), "course":class_detail}
    return render(request, 'webapp/classdetail.html',context)

# 服务页面
def Service(request):
    context = {"form":signincore(request)}

    return render(request, 'webapp/service.html',context)

# 首页
def index(request):
    all_course = Course.objects.all()
    context = {"form": signincore(request),"all_courses":all_course}

    return render(request, 'webapp/index.html',context)

def newIndex(request):
    all_course = Course.objects.all()
    context = {"form": signincore(request),"all_courses":all_course}
    return render(request, 'webapp/newIndex.html', context)