from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .forms import UserIDForm, VitaminForm 
from .models import User, VitaminData
from django.forms.models import modelformset_factory, inlineformset_factory
from django.forms import formset_factory
# Create your views here.
def identification(request):
    #Present ID page to user and save info
    iform = UserIDForm(request.POST or None)
    if iform.is_valid():
        user_id = iform.cleaned_data['Identification_Number']
        user_id_repeat = iform.cleaned_data['Please_repeat_Identification_Number']
        save_it=iform.save(commit=False)
        request.session['testing']=user_id_repeat
        if str(user_id)==user_id_repeat:
            save_it.save()
            return HttpResponseRedirect("vitamins")
        else:
            return HttpResponse("Identification Numbers are not equal. Please try again.")
    context ={"iform": iform,}
    template = "identification.html"
    return render(request,template,context)
    
def vitamins(request):
    VitaminList=["Vitamin_A", "Pottasium"]
    VitaminFormset=modelformset_factory(VitaminData, form=VitaminForm)
    #pull ID object from Identify table
    if 'testing' in request.session:
        user_id_repeat=request.session['testing']
        user_object= get_object_or_404(User, pk=user_id_repeat)
    #Present vitamin form to user and save info with ID tag 
    #vform = VitaminForm(request.POST or None)
    formset=VitaminFormset(request.POST or None)
    if formset.is_valid():
  #      save_it=formset.save(commit=False)
        #save_it.vitamin_Name=x
  #      save_it.save()
        return HttpResponse("This might have worked")
    context ={"formset": formset,"VitaminList": VitaminList }
    template = "vitamins.html"
    return render(request,template,context)
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
