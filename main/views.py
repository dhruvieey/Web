import base64
from email.mime import image
import re
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render,HttpResponse
from django.contrib.auth.models import User,auth
from .models import EditProfile, Post
from .forms import AddPostForm, EditProfileForm, profileForm
import speech_recognition as sr
# Create your views here.
def index(request):
    return render(request,'index.html')

def homeView(request):
    if not request.user.is_authenticated:
        return redirect('login')

    current_user = request.GET.get('user')
    logged_in_user = request.user.username
    return render(request, 'home.html' , {'current_user':logged_in_user})

def logoutUser(request):
    auth.logout(request)
    return redirect('login')

def registration(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST' :
        firstName = request.POST['firstName']
        lastName = request.POST['lastName']
        userName = request.POST['userName']
        email = request.POST['email']
        password = request.POST['password1']
        confirmPassword = request.POST['password2']
        if password == confirmPassword:
            if User.objects.filter(username=userName).exists():
                messages.error(request, 'username not available')
                return redirect('register')
            else:
                user = User.objects.create_user(username=userName, first_name=firstName,last_name=lastName,email=email,password=password)
                user.save()
                EditProfile.objects.create(user=user)
                auth.login(request, user)
                return redirect('home')
        else :
            messages.error(request,' password not matched ')
            return redirect('register')
            
    else:
        return render(request, 'register.html')


def login(request):
    if request.user.is_authenticated:
        return redirect("home")
    if request.method == 'POST':
        username = request.POST['userName']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.error(request,'invalid username or password')
            return redirect('login')
    else:
        return render(request, 'login.html')

def profile(request):
    author = User.objects.get(username=request.user.username)
    post = reversed(Post.objects.filter(author=author))
    data = EditProfile.objects.get(user = request.user)
    return render(request, 'profile.html', {'data' : data, 'post':post})

def edit_profile(request):
    profile = EditProfile.objects.get(user = request.user)
    form2 = profileForm(instance=request.user)
    form = EditProfileForm( instance = profile)
    if request.method == 'POST':
        form = EditProfileForm( request.POST, request.FILES, instance = profile)
        form2 = profileForm(request.POST,instance=request.user)
        if form.is_valid() and form2.is_valid():
            form.save()
            form2.save()
            return redirect('user_profile')
    context = {'form':form, 'form2':form2}
    return render(request, 'edit-profile.html',context)

def guess_the_word(request):
        return render(request,'guess_the_word.html')

def multiplication_game(request):
        return render(request,'multiplication_game.html')

def save_recorded_audio(request):
    if request.method == "POST":
        print("Start")
        audio_file = request.FILES.get("audio")
        print("Audio Gen")
        recognizer = sr.Recognizer()
        print("Recognizer Activated")
        audio_data = sr.AudioData(audio_file.read(), audio_file.samplerate, audio_file.sample_width)
        print("Audio Data Taken")
        text = recognizer.recognize_google(audio_data)
        print("Text Gen")
        print(text)
        return HttpResponse("Audio uploaded successfully")
    else:
        return render(request,'voice.html')
    
def maze(request):
    return render(request,'maze.html')

def crossword(request):
    return render(request,'crossword-puzzle-demo.html')
