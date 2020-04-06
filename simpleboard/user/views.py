from django.shortcuts import render, redirect

# Create your views here.
def login(request):
  return render(request,'login.html')

def dologin(request):
  return redirect('/board/main')

def signup(request):
  return render(request,'signup.html')

def dosignup(request):
  return redirect('/user/login') 