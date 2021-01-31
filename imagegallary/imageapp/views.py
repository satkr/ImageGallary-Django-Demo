from django.http import HttpResponse
from django.shortcuts import render, redirect
from imageapp.models import Image
from imageapp.forms import ImageForm, FilterForm
from django.core.paginator import Paginator


# Create your views here.
def index(request):
    imgform = ImageForm()
    filterform = FilterForm()
    img=[]
    if request.method == 'POST':
        imgform = ImageForm(request.POST, request.FILES)
        filterform = FilterForm(request.POST)
        img = Image.objects.all()
        if imgform.is_valid():
            imgform.save()
            imgform = ImageForm()
            return render(request, 'index.html', {'imgform': imgform, 'filterform': filterform, 'img': img})
        if filterform.is_valid():
            if str(request.POST['filter']) == 'all':
                img = Image.objects.all()
            else:
                img = Image.objects.filter(category=str(request.POST['filter']))
            filterform = FilterForm()
            imgform = ImageForm()
            return render(request, 'index.html', {'imgform': imgform,'filterform': filterform, 'img': img})
    try:
        if request.method == 'GET':
            img = Image.objects.all()
        return render(request, 'index.html', {'imgform': imgform,'filterform': filterform, 'img': img})
    except:
        return render(request, 'index.html', {'imgform': imgform,'filterform': filterform})


def success(request):
    return HttpResponse('successfully uploaded')