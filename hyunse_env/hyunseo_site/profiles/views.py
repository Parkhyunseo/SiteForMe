from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.http import HttpResponse

# Create your views here.

from .models import Task
from .forms import TaskForm

from datetime import datetime

def home(request):
    if request.method == "GET":
        form = TaskForm()
    elif request.method == "POST":
        form = TaskForm(request.POST)
        
        if form.is_valid():
            obj = form.save(commit=False)
            obj.content = request.POST['content']
            obj.dueto = request.POST['duedate']
            obj.tag = request.POST['tag']
            obj.save()
            
            form = TaskForm()
    
    task_list = Task.objects.order_by('-created_at')
    now = datetime.now()
    
    ctx = {
        'form' : form,
        'tasks' : task_list,
        'today' : now.strftime('%d %B, %Y')
    }
        
    return render(request, 'profiles.html', ctx)

def taskcheck(request):
    return HttpResponse(request, content_type="application/json")