from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
# Create your views here.
from django.urls import path
from .forms import PhoneForm
from phone.models import PhoneModel

from . import views

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
    
def get_phone(request):
    if request.method == 'POST':
        form = PhoneForm(request.POST)
        if form.is_valid():
            PhoneForm.save(form)
            return HttpResponseRedirect('/phone_form')
    else:
        form = PhoneForm()
    return render(request, 'phone/phone_form.html', {'form':form})

def get_data(request):
    if request.method == 'GET':
        data = PhoneModel.objects.values()
        print(data)
        return render(request,'phone/table.html', {"data":list(data)})