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
    if 'testing' in request.session:
        user_id_repeat=request.session['testing']
        user_object=get_object_or_404(User, pk=user_id_repeat)
    i=0
    fruitList=["Rasins (1.oz or small pack) or grapes(1/2 cup)", "Prunes or dried plums (6 prunes or 1/4 cup)","Prune juice (small glass)","Bananas (1)","Cantaloupe (1/4 melon)","Avocado (1/2 fruit or 1/2 cup)", "Fresh apples or pears(1)", "Apple juice or cider (small glass)","Orange juice (small glass): Calcium foritifed", "Orange juice (small glass): Regular (not calcium foritifed)", "Grapefruit (1/2) or grapefruit juice (small glass)", "Other fruit juices (small glass)", "Strawberries, fresh, frozen or canned (1/2 cup)", "Blueberries, fresh, frozen or canned (1/2 cup)", "Peaches or plums (1 fresh or 1/2 cup canned)", "Apricots (1 fresh, 1/2 cup canned or 5 dried)"]
    fruitFormset=formset_factory(FoodForm, extra=len(fruitList))
    formset=fruitFormset(request.POST or None)
    formzip=zip(formset, fruitList)
    last=len(formset)
    for form in formset.forms:
        if form.is_valid():
            freq=form.cleaned_data['food_freq']
            new_data=FoodData(user=user_object, food_freq=freq, food_name=fruitList[i])
            i=i+1
            new_data.save()
            if i==last:
                return HttpResponseRedirect('vegetables')
    context ={"formset": formset, "fruitList": fruitList, "formzip":formzip, "freq_options": freq_options,}
    template = "fruits.html"
    return render(request,template,context)
def vegetables(request):
    if 'testing' in request.session:
        user_id_repeat=request.session['testing']
        user_object=get_object_or_404(User, pk=user_id_repeat)
    i=0
    vegetableList=["Tomatoes (2 slices)","Tomato or V-8 juice (small glass)","Tomato sauce (1/2 cup) e.g., spaghetti sauce","Salsa, picante or taco sauce (1/4 cup)","String beans (1/2 cup)","Beans or lentils, baked, dried or soup (1/2 cup)","Tofu, soy burger, soybeans, miso or other soy protein","Peas or lima beans (1/2 cup fresh, frozen, canned)","Broccoli (1/2 cup)", "Cauliflower (1/2 cup)","Cabbage or coleslaw (1/2 cup)","Brussels sprouts (1/2 cup)","Carrots, raw (1/2 carrot or 2-4 sticks)","Carrots, cooked (1/2 cup) or carrot juice (2-3 oz.)","Corn (1 ear or 1/2 cup frozen or canned)","Mixed or stir-fry vegetables (1/2 cup), veg. soup (1 cup)","Yams or sweet potatoes (1/2 cup)","Dark orange (winter) squash (1/2 cup)","Eggplant, zucchini or other summer squash (1/2 cup)","Kale, mustard greens or chard (1/2 cup)""Spinach, cooked (1/2 cup)","Spinach, raw as in salad (1 cup)","Iceberg or head lettuce (1 serving)", "Romaine or leaf lettuce (1 serving)","Celery (2-3 sticks)","Peppers: green, yellow or red (3 slices)","Onions as a garnish or in salad (1 slice)","Onions as a cooked vegetable, rings or soup (1/2 cup)"]
    vegetableFormset=formset_factory(FoodForm, extra=len(vegetableList))
    formset=vegetableFormset(request.POST or None)
    formzip=zip(formset, vegetableList)
    last=len(formset)
    for form in formset.forms:
        if form.is_valid():
            freq=form.cleaned_data['food_freq']
            new_data=FoodData(user=user_object, food_freq=freq, food_name=vegetableList[i])
            i=i+1
            new_data.save()
            if i==last:
                return HttpResponseRedirect('eggsmeat')
    context ={"formset": formset, "vegetableList": vegetableList, "formzip":formzip, "freq_options": freq_options,}
    template = "vegetable.html"
    return render(request,template,context)
def eggsmeat(request):
    if 'testing' in request.session:
        user_id_repeat=request.session['testing']
        user_object=get_object_or_404(User, pk=user_id_repeat)
    i=0
    eggsmeatList=["Eggs (1): Omega-3 fortified including yolk","Eggs (1): Regular eggs including yolk","Beef or pork hot dogs (1)","Chicken or turkey hot dogs or sausage (1)","Chicken/turkey sandwich or frozen dinner","Other chicken or turkey, with skin (3 oz.)","Other chicken or turkey, without skin (3 oz.)- including ground","Bacon (2 slices)","Salami, bologna, or other processed meat sandwiches","Other processed meats, e.g., sausage, kielbasa,etc. (2 oz. or 2 small links)","Hamburger (1 patty): Lean or extra lean","Hamburger (1 patty): Regular","Beef, pork, or lamb as a sandwich or mixed dish, e.g., stew, casserole, lasagna, frozen dinners, etc.","Pork as a main dish, e.g., ham or chops (46 oz.)","Beef or lamb as a main dish, e.g., steak, roast (46 oz.)","Canned tuna fish (34 oz.)","Breaded fish cakes, pieces, or fish sticks","Shrimp, lobster, scallops as a main dish","Dark meat fish, e.g., tuna steak, mackerel, salmon, sardines, bluefish, swordfish (35 oz.)","Other fish, e.g., cod, haddock, halibut (35 oz.)"]
    eggsmeatFormset=formset_factory(FoodForm, extra=len(eggsmeatList))
    formset=eggsmeatFormset(request.POST or None)
    formzip=zip(formset, eggsmeatList)
    last=len(formset)
    for form in formset.forms:
        if form.is_valid():
            freq=form.cleaned_data['food_freq']
            new_data=FoodData(user=user_object, food_freq=freq, food_name=eggsmeatList[i])
            i=i+1
            new_data.save()
            if i==last:
                return HttpResponseRedirect('carbs')
    context ={"formset": formset, "eggsmeatList": eggsmeatList, "formzip":formzip, "freq_options": freq_options,}
    template = "eggsmeat.html"
    return render(request,template,context)
def carbs(request):
    if 'testing' in request.session:
        user_id_repeat=request.session['testing']
        user_object=get_object_or_404(User, pk=user_id_repeat)
    i=0
    carbsList=["Cold breakfast cereal (1 serving)","Cooked oatmeal/cooked oat bran (1 cup)","Other cooked breakfast cereal (1 cup)","Bread (1 slice): White bread, including pita","Bread (1 slice): Rye/Pumpernickel","Bread (1 slice): Whole wheat, oatmeal, other whole grain","Crackers, regular or lowfat e.g., Triscuits, Ritz (6)","Bagels, English muffins, or rolls (1)","Muffins or biscuits (1)","Pancakes or waffles (2 small pieces)","Brown rice (1 cup)","White rice (1 cup)","Pasta, e.g., spaghetti, noodles, couscous, etc. (1 cup)","Tortillas (2)","French Fries (6 oz. or 1 serving)","Potatoes, baked, boiled (1) or mashed (1 cup)","Potato chips or corn/tortilla chips (small bag or 1 oz.)","Pizza (2 slices)"]
    carbsFormset=formset_factory(FoodForm, extra=len(carbsList))
    formset=carbsFormset(request.POST or None)
    formzip=zip(formset, carbsList)
    last=len(formset)
    for form in formset.forms:
        if form.is_valid():
            freq=form.cleaned_data['food_freq']
            new_data=FoodData(user=user_object, food_freq=freq, food_name=carbsList[i])
            i=i+1
            new_data.save()
            if i==last:
                return HttpResponseRedirect('beverages')
    context ={"formset": formset, "carbsList": carbsList, "formzip":formzip, "freq_options": freq_options,}
    template = "carbs.html"
    return render(request,template,context)
def beverages(request):
    if 'testing' in request.session:
        user_id_repeat=request.session['testing']
        user_object=get_object_or_404(User, pk=user_id_repeat)
    i=0
    beveragesList=["Low-calorie beverage with caffeine, e.g., Diet Coke, Diet Mt. Dew","Other low-cal bev. without caffeine, e.g., Diet 7-Up","Carbonated beverage with caffeine & sugar, e.g., Coke, Pepsi, Mt. Dew, Dr. Pepper","Other carbonated beverage with sugar, e.g., 7-Up, Root Beer, Ginger Ale, Caffeine-Free Coke","Other sugared beverages: Punch, lemonade, sports drinks, or sugared ice tea (1 glass, bottle, can)","Beer, regular (1 glass, bottle, can)","Light Beer, e.g., Bud Light (1 glass, bottle, can)","Red wine (5 oz. glass)","White wine (5 oz. glass)","Liquor, e.g., vodka, gin, etc. (1 drink or shot)","Water: bottled, sparkling, or tap (8 oz. cup)","Herbal tea or decaffeinated tea (8 oz. cup)","Tea with caffeine (8 oz. cup), including green tea","Decaffeinated coffee (8 oz. cup)","Coffee with caffeine (8 oz. cup)","Dairy coffee drink (hot/cold) e.g., Cappuccino (16 oz.)"]
    beveragesFormset=formset_factory(FoodForm, extra=len(beveragesList))
    formset=beveragesFormset(request.POST or None)
    formzip=zip(formset, beveragesList)
    last=len(formset)
    for form in formset.forms:
        if form.is_valid():
            freq=form.cleaned_data['food_freq']
            new_data=FoodData(user=user_object, food_freq=freq, food_name=beveragesList[i])
            i=i+1
            new_data.save()
            if i==last:
                return HttpResponseRedirect('sweetsetc')
    context ={"formset": formset, "beveragesList": beveragesList, "formzip":formzip, "freq_options": freq_options,}
    template = "beverages.html"
    return render(request,template,context)
    return HttpResponse("Beverages questions go here")
def sweetsetc(request):
    context ={}
    template = ""
    return HttpResponse("Sweets questions go here")
def genq2(request):
    context ={}
    template = ""
    return HttpResponse("Final general questions go here")
