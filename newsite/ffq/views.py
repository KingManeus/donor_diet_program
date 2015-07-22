from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .forms import UserIDForm, VitaminForm, FoodForm
from .models import User, VitaminData, FoodData
from django.forms.models import modelformset_factory, inlineformset_factory
from django.forms import formset_factory
freq_options=["","Never, or less than once per month", "1-3 per month", "1 per week", "2-4 per week", "5-6 per week", "1 per day", "2-3 per day", "4-5 per day", "6+ per day"]
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
    VitaminList=["Vitamin A", "Pottasium", "Vitamin C", "Vitamin B6", "Vitamin E", "Calcium", "Selenium", "Vitamin D", "Zinc"]
    vitaminFormset=formset_factory(VitaminForm, extra=len(VitaminList))
 
    #pull ID object from Identify table
    if 'testing' in request.session:
        user_id_repeat=request.session['testing']
        user_object= get_object_or_404(User, pk=user_id_repeat)
    #Present vitamin form to user and save info with ID tag 
    #vform = VitaminForm(request.POST or None)
    i=0
    formset=vitaminFormset(request.POST or None)
    formzip=zip(formset,VitaminList)
    last = len(formset)-1
    for form in formset.forms:
        if form.is_valid():
            amount=form.cleaned_data['vitamin_Amount']
            boolean=form.cleaned_data['vitamin_Boolean']
            new_data=VitaminData(user=user_object, vitamin_Boolean=boolean, vitamin_Amount=amount, vitamin_Name=VitaminList[i])
            i=i+1
            new_data.save()
            if i==last:
                return HttpResponseRedirect("genq")
    context ={"formset": formset,"VitaminList": VitaminList, "formzip": formzip}
    template = "vitamins.html"
    return render(request,template,context)
def genq(request):
    context ={}
    template = ""
    return HttpResponse("Some general questions go here")
def dairy(request):
    if 'testing' in request.session:
        user_id_repeat=request.session['testing']
        user_object=get_object_or_404(User, pk=user_id_repeat)
    i=0
    dairyList=["Skim Milk (8.oz glass)","1 or 2%% Milk (8.oz glass)", "Whole Milk (8.oz glass)", "Soy Milk (8.oz glass)", "Cream, eg. coffee, whipped or sour cream (1 Tbs)","Non-dairy coffee whitener (1 Tbs)", "Frozen yogurt, sherbet or low-fat ice cream (1 cup)","Regular ice cream (1 cup)","Yogurt (1 cup): Low-carb, artificially sweetened or plain","Yogurt (1 cup): Sweetened-with fruit or other flavoring","Margarine","Pure Butter", "Cottage or ricotta cheese (1/2 cup)", "Cream cheese (1 oz.)","Other cheese, e.g., American, cheddar, etc., plain or as part of a dish (1 slice or 1 oz. serving)"]
    dairyFormset=formset_factory(FoodForm, extra=len(dairyList))
    formset=dairyFormset(request.POST or None)
    formzip=zip(formset, dairyList)
    last=len(formset)
    for form in formset.forms:
        if form.is_valid():
            freq=form.cleaned_data['food_freq']
            new_data=FoodData(user=user_object, food_freq=freq, food_name=dairyList[i])
            i=i+1
            new_data.save()
            if i==last:
                return HttpResponseRedirect('fruits')
    context ={"formset": formset, "dairyList": dairyList, "formzip":formzip, "freq_options": freq_options,}
    template = "dairy.html"
    return render(request,template,context)
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
