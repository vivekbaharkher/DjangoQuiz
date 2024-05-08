import profile
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Profile
from django.http import HttpResponse
from .models import Question,Choice,Quiz
from django.contrib.auth import authenticate,login,logout
from .forms import QuizForm, QuestionForm, ChoiceForm
from .models import Quiz
from django.urls import reverse


# Create your views here.
# def quizz(request):
#     questions = Question.objects.all()
#     return render (request,'quizz.html',{'questions':questions})

# @login_required(login_url="login")
# def home(request):
#     profile = Profile.objects.get(user=request.user)
#     if profile.played:
#         return HttpResponse(f"You have already played the game.<br> Your score: {profile.score}")
#     else:
#         questions = Question.objects.all()
#         score = 0
#         if request.method == 'POST':
#             total_questions = Question.objects.count()
#             for question in questions:
#                 selected_choice_id = request.POST.get(f'question{question.id}')
#                 if selected_choice_id is not None:
#                     correct_choice = Choice.objects.get(question=question, is_correct=True)
#                     if int(selected_choice_id) == correct_choice.id:
#                         score += 1
#                         print(score)
#                         profile.score = score
#                         profile.played= True
#                         profile.save()
#     return render(request, 'home.html', {'questions': questions,'score':score})
@login_required(login_url="login")
def main(request):
    try:
        quizs = Quiz.objects.filter(user=request.user)
        
    except:
        quizs = []
    return render(request,'main.html',{'quizs':quizs})


def register(request):
    if request.method == 'POST':
        username= request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        firstname=request.POST.get('firstname')
        lastname=request.POST.get('lastname')
        User.objects.create_user(username=username,
                                password=password,
                                #  firstname=firstname,
                                #  lastname=lastname,
                                email=email)
        return redirect('main')
    return render(request,'register.html')

def loggin(request):
    if request.user.is_authenticated:
        return redirect('main')
    else:
        if request.method == 'POST':
            username=request.POST.get('username')
            password=request.POST.get('password')
            email=request.POST.get('email')
            user= authenticate(request,
                                username=username,
                                password=password,
                                email=email)
            if user is not None:
                login(request,user)
                return redirect('/main')
        return render(request,'login.html')

def logoutt(request):
    logout(request)
    return redirect('/main')

def update(request,id):
    quiz=Quiz.objects.get(id=id)
    form=QuizForm(instance=quiz)
    if request.user == quiz.user:
        if request.method=='POST':
            form=QuizForm(request.POST,instance=quiz)
            if form.is_valid():
                form.save()
                return redirect('/main')
    else:
        return redirect ('login')
        # return HttpResponse("You are not the user")
    return render(request,'quiz_topic.html',{'form':form})
def delete(request,id):
        quiz =Quiz.objects.get(id=id)
        form=QuizForm(instance=quiz)
        if request.user == quiz.user:
            quiz.delete()
        else:
            return redirect("/login")
        return render(request,'main.html',{'quiz':quiz})

@login_required(login_url="login")
def create_topic(request):
    form=QuizForm()
    if request.method=='POST':
        # print(request.POST)
        form = QuizForm(request.POST)
        if form.is_valid():
            quiz = form.save(commit=False)
            quiz.user = request.user
            quiz = form.save()
            return redirect('/main')
    return render(request,'quiz_topic.html',{'form':form})

@login_required(login_url="login")
def add_question(request,id):
    quiz = Quiz.objects.get(id=id)
    form = QuestionForm()
    if request.method == "POST":
        
        form = QuestionForm(request.POST)
        if form.is_valid():
            question_obj = form.save(commit=False)
            question_obj.quiz = quiz
            question_obj.save()
            return redirect(f'/list_questions/{id}/')
        
    context = {
        'quiz':quiz,
        'form':form
    }
    return render(request,'add_question.html',context)

def add_options_by_question(request,id):
    question = Question.objects.get(id=id)
    quiz_id = question.quiz.id
    form = ChoiceForm()
    if request.method == "POST":
        
        form = ChoiceForm(request.POST)
        if form.is_valid():
            choice_obj = form.save(commit=False)
            choice_obj.question = question
            choice_obj.save()
            return redirect(f'/list_questions/{quiz_id}/')
        
    context = {
        'question':question,
        'form':form
    }
    return render(request,'add_options.html',context)

def list_question_by_quiz(request,id):
    quiz = Quiz.objects.get(id=id)
    questions = Question.objects.filter(quiz=quiz)
    score = 0
    if request.method == "POST":
        for question in questions:
            selected_choice_id=request.POST.get(f'question{question.id}')
            if selected_choice_id is not None:
                correct_choice = Choice.objects.get(question=question, is_correct=True)
                if int (selected_choice_id)==correct_choice.id:
                    score+=1
                    print(score)
                    profile.score = score
                    # profile.played= True
                    # profile.save()
                    return redirect('/list_questions')
    context = {
        'questions':questions,
        'quiz':quiz,
        'score':score
    }
    return render(request,'listquestion.html',context)
    