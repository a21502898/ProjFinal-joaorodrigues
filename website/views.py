from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import login, logout
from .forms import UserDataForm, CreateComment
from django.http import HttpResponseRedirect
from .models import Comments
from django.contrib.auth.decorators import login_required


def base_page_view(request):
    return render(request, 'website/base.html', )

def home_page_view(request):
    return render(request, 'website/home.html', )

def signup_page_view(request):
    if request.method =='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'!!User has been registred!!.')
            return redirect('/login')
    else:
        form = UserCreationForm()
    return render(request, 'website/signup.html', {'form': form})

def login_page_view(request):
    if request.method=="POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/home')
    else:
        form = AuthenticationForm()
    return render(request, 'website/login.html', {'form':form})

def myinfo_page_view(request):
    submitted = False
    if request.method == "POST":
        form = UserDataForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect ('/myinfo?submitted=True')
    else:
        form = UserDataForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'website/myinfo.html', {'form':form, 'submitetd':submitted})

def logout_page_view(request):
    if request.method == 'POST':
        logout(request)
    return redirect("/home")

def comments_list_page_view(request):
    comments = Comments.objects.all().order_by('date');
    return render(request, 'website/comment-list.html', {'comments':comments} )

#@login_required(login_url='/login')
def create_comment_page_view(request):
    if request.method == 'POST':
        form = CreateComment(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('website:comment-list')
    else:
        form = CreateComment
    return render(request, 'website/create-comment.html', {'form':form})


def mtb_page_view(request):
    return render(request, 'website/MTB/MTBPage.html', )

def road_page_view(request):
    return render(request, 'website/BMX/BMXPage.html', )

def bmx_page_view(request):
    return render(request, 'website/RB/RBPage.html', )

