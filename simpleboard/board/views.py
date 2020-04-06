from django.shortcuts import render, redirect

# Create your views here.
def main(request):
  return render(request,'board.html')

def detail(request):
  return render(request, 'detail.html')

def editBoard(request):
  return render(request, 'edit.html')

def edit(request):
  return redirect('/board/detail')

def add(request):
  return redirect('/board/main')

def remove(request):
  return redirect('/board/main')