from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.http import HttpResponse

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

#from .forms forms 생성

# Create your views here.
def dv(request):
    return render(request, 'datavisual.html')
