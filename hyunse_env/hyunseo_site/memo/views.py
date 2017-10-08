from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.http import HttpResponse
#from django.contrib.auth.decorators import login_required

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Memo
from .forms import MemoForms
#from .forms forms 생성

# Create your views here.
def memo_view(request):
    #real infinite logic
    
    # ------ MEMO -----------
    memo_list = Memo.objects.order_by('-created_at')
   
    #infinite sample
    #numbers_list = [ 'a' for _ in range(1000)] # range
    #page = request.GET.get('page', 1) # url
    #paginator = Paginator(numbers_list, 20) # n개씩
    
    page = request.GET.get('page', 1) # url
    paginator = Paginator(memo_list, 20)
    
    try:
        memos = paginator.page(page)
    except PageNotAnInteger: # If not Integer
        memos = paginator.page(1)
    except EmptyPage: 
        memos = paginator.page(paginator.num_pages)
    
    # -------- MEMO FORM -----------
    if request.method == "GET":
        form = MemoForms()
        #print(form)
    elif request.method == "POST":
        form = MemoForms(request.POST)
        print(form)
        
        if form.is_valid():
            obj = form.save(commit=False)
            obj.content = request.POST['content']
            obj.content_color = request.POST['content_color']
            obj.save()
            form = MemoForms()
            
    ctx = {
            'memos' : memos,
            'form': form,
    }

    return render(request, 'memo.html', ctx)
    
#not use
def create(request):
    memos = Memo.objects.order_by('created_at')
        
    if request.method == "GET":
        print("GET")
        form = MemoForms()
        #print(form)
    elif request.method == "POST":
        print("POST")
        form = MemoForms(request.POST)
        print(form)
        
        if form.is_valid():
            print("ISVALID")
            obj = form.save(commit=False)
            obj.content = request.POST["memo_text"]
            obj.save()
            
            ctx = {
                'memos' : memos,
                'form': form,
            }
            
            return redirect('memo.html', ctx)
            
    ctx = {
        'memos' : memos,
        'form': form,
    }
    
    return render(request, 'memo.html', ctx)
