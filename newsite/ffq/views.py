from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import IForm, TestChoice
from .models import Identify, Question, Choice
# Create your views here.
def identification(request):
    iform = IForm(request.POST or None)
    #testform=TestChoice()
    if iform.is_valid():
        iNumber = iform.cleaned_data['iNumber']
        iNumberRepeat = iform.cleaned_data['iNumberRepeat']
        save_it=iform.save(commit=False)
        if str(iNumber)==iNumberRepeat:
            save_it.save()
            return HttpResponseRedirect("vitamins")
        else:
            return HttpResponse("Identification Numbers are not equal. Please try again.")
    context ={"iform": iform,}
    template = "identification.html"
    return render(request,template,context)
def vitamins(request):
    context ={}
    template = ""
    return HttpResponse("Vitamin questions go here")
def genq(request):
    context ={}
    template = ""
    return HttpResponse("Some general questions go here")
def dairy(request):
    context ={}
    template = ""
    return HttpResponse("Dairy questions go here")
def fruits(request):
    context ={}
    template = ""
    return HttpResponse("Fruit questions go here")
def vegetables(request):
    context ={}
    template = ""
    return HttpResponse("Vegetables questions go here")
def eggsmeat(request):
    context ={}
    template = ""
    return HttpResponse("Eggs, meat, etc questions go here")
def carbs(request):
    context ={}
    template = ""
    return HttpResponse("Carbs questions go here")
def beverages(request):
    context ={}
    template = ""
    return HttpResponse("Beverages questions go here")
def sweetsetc(request):
    context ={}
    template = ""
    return HttpResponse("Sweets questions go here")
def genq2(request):
    context ={}
    template = ""
    return HttpResponse("Final general questions go here")
