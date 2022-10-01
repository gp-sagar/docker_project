from django.shortcuts import render, redirect
from .forms import *
from django.contrib import messages

# Create your views here.

def home(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Form Submitted Successfully')
        return redirect('/')
    return render(request, 'index.html')
