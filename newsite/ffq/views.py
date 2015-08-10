from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .forms import UserIDForm, VitaminForm, FoodForm, VitTotalChoices, MultiForm, BackForm
from .models import User, VitaminData, FoodData
from django.forms.models import modelformset_factory, inlineformset_factory
from django.forms import formset_factory
freq_options=["Never, or less than once per month", "1-3 per month", "1 per week", "2-4 per week", "5-6 per week", "1 per day", "2-3 per day", "4-5 per day", "6+ per day"]
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
            return HttpResponseRedirect("eggsmeat")
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
    i=0
    mform=MultiForm(request.POST or None)
    formset=vitaminFormset(request.POST or None)
    formzip=zip(formset,VitaminList, VitTotalChoices)
    last = len(formset)
    for form in formset.forms:
        if form.is_valid():
            amount=form.cleaned_data['vitamin_Amount']
            boolean=form.cleaned_data['vitamin_Boolean']
            new_data=VitaminData(user=user_object, vitamin_Boolean=boolean, vitamin_Amount=amount, vitamin_Name=VitaminList[i],)
            i=i+1
            new_data.save()
            if i==last:
                return HttpResponseRedirect("genq")
    context ={"formset": formset,"VitaminList": VitaminList, "formzip": formzip, "VitTotalChoices": VitTotalChoices, "mform": mform,}
    template = "vitamins.html"
    return render(request,template,context)
def genq(request):
    form=BackForm(request.POST or None)
    context ={"form":form}
    template = "genq.html"
    return render(request,template,context)
def dairy(request):
    if 'testing' in request.session:
        user_id_repeat=request.session['testing']
        user_object=get_object_or_404(User, pk=user_id_repeat)
    i=0
    dairyList=["Cream or sour cream (tablespoon)", "Creme Fraiche or clotted cream (tablespoon)", "Low-fat yogurt (4oz)", "Full-fat Greek Yogurt (4oz)", "Dairy Desserts (4oz)", "Cheese, eg. Cheddar, Brie, Edam (medium serving)", "Cottage cheese, low fat soft cheese (medium serving)", "Eggs as boiled, fried, scrambled, etc. (one)", "Quiche (medium serving)", "Low calorie, low fat creamy dressing (tablespoon)", "Creamy dressing, mayonnaise (tablespoon)", "French dressing (tablespoon)", "Other salad dressing (tablespoon)", "Butter (teaspoon)", "Block margarine (teaspoon)", "Tub margarine made from sunflower, canola, olive oil (teaspoon)", "Other tub margarine (teaspoon)", "Low-fat butter substitute (teaspoon)", "Very low-fat or non-butter substitute (teaspoon)"]
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
                return HttpResponseRedirect('sweetsetc')
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
    vegetableList=["Carrots", "Spinach", "Broccoli, mustard greens, kale", "Brussels sprouts", "Cabbage", "Peas", "Green beans, fava beans, French beans", "Squash", "Cauliflower", "Parsnips, turnips, rutabaga", "Leeks", "Onions", "Garlic", "Mushrooms", "Bell peppers", "Beansprouts", "Green salad, lettuce, cucumber, celery", "Watercress", "Tomatoes", "Corn", "Beet", "Coleslaw", "Avocado", "Baked beans", "Dried lentis, beans, peas", "Tofu, soy protein, vegetable burger"]
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
                return HttpResponseRedirect('genq')
    context ={"formset": formset, "vegetableList": vegetableList, "formzip":formzip, "freq_options": freq_options,}
    template = "vegetable.html"
    return render(request,template,context)
def eggsmeat(request):
    if 'testing' in request.session:
        user_id_repeat=request.session['testing']
        user_object=get_object_or_404(User, pk=user_id_repeat)
    i=0
    eggsmeatList=["Beef: roast, steak, mince, stew or casserole","Beefburgers", "Pork: roast, chops, stew or slices", "Lamb: roast, chops or stew", "Chiken or other poultry eg. turkey", "Bacon", "Ham", "Corned beef, Spam, luncheon meats", "Sausages", "Meat pies, meat rolls", "Liver, liver pate, liver sausage", "Fried fish in batter, as in fish and chips", "Fish fingers, fish cakes", "Other white fish, fresh or frozen, eg. cod, haddock, plaice, sole halibut", "Oily fish, fresh or canned, eg. mackerel, kippers, tuna, salmon, sardines, herring", "Shellfish, eg. crabs, shrimp, mussels", "Fish roe, taramasalata"]
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
    carbsList=["White bread and rolls", "Rye/pumpernickel bread and rolls", "Whole wheat bread and rolls", "Crackers", "Rye crisp", "Hot cereal", "Cold cereal", "Boiled, mashed, instant or jacket potatoes", "French fries", "Roast potatoes", "Potato salad", "White rice", "Brown rice", "White or green pasta, eg. spaghetti, macaroni, noodles", "Whole wheat pasta", "Lasagne, moussaka", "Pizza"]
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
                return HttpResponseRedirect('dairy')
    context ={"formset": formset, "carbsList": carbsList, "formzip":formzip, "freq_options": freq_options,}
    template = "carbs.html"
    return render(request,template,context)
def beverages(request):
    if 'testing' in request.session:
        user_id_repeat=request.session['testing']
        user_object=get_object_or_404(User, pk=user_id_repeat)
    i=0
    beveragesList=["Tea (cup)", "Coffee, instant or ground (cup)", "Coffee, decaffeinated (cup)", "Coffee whitener, eg. Cofee-mate (teaspoon)", "Cocoa, hot chocolate (cup)", "Milkshake, eg. Ovaltine (cup)", "Wine (glass)", "Beer, lager or cider (half pint)", "Port, sherry, vermouth, liquers (glass)", "Spirits, eg. gin, brandy, whisky, vodka (single)", "Low calorie or diet sodas (glass)", "Regular sodas (glass)", "Pure fruit juice (100%) eg. orange, apple juice (glass)", "Fruit squash or cordial (glass)", "Apples (1 fruit)", "Pears (1 fruit)", "Oranges, clementines, mandarins (1 fruit)", "Grapefruit (half)", "Bananas (1 fruit)", "Grapes (medium serving)", "Melon (1 slice)", "* Peaches, plums, apricots (1 fruit)", "* Strawberries, raspberries, kiwi fruit (medium serving)", "Canned fruit (medium serving)", "Dried fruit, eg. raisins, prunes (medium serving)"]
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
                return HttpResponseRedirect('vegetables')
    context ={"formset": formset, "beveragesList": beveragesList, "formzip":formzip, "freq_options": freq_options,}
    template = "beverages.html"
    return render(request,template,context)
def sweetsetc(request):
    if 'testing' in request.session:
        user_id_repeat=request.session['testing']
        user_object=get_object_or_404(User, pk=user_id_repeat)
    i=0
    sweetsList=["Chocolate cookie (one)", "Plain cookie (one)", "Cakes eg. fruit, sponge, home baked", "Cakes eg. fruit, sponge, ready made", "Buns, pastries eg. scones, pancakes, home baked", "Bunds, pastries eg. croissants, doughnuts, ready made","Fruit pies, tarts, crumbles, home baked", "Fruit pies, tarts, crumbles, ready made", "Sponge puddings, home baked", "Sponge pudings, ready made", "Milk puddings and custards", "Ice cream, chocolate ices", "Chocolates, single or squares","Chocolate candy bars", "Sweets, tofees, mints", "Sugar added to tea, coffee, cereal (teaspoon)", "Potato chips or other bagged snacks", "Peanuts or other nuts", "Vegetable soups (bowl)", "Meat soups (bowl)", "Sauces, eg. white sauce, cheese sauce, gravy (tablespoon)", "Ketchup (tablespoon)", "Pickles, chutney (tablespoon)", "Marmite, Bovril (teaspoon)", "Jam, marmalade, honey (teaspoon)", "Peanut Butter (teaspoon)"]
    sweetsFormset=formset_factory(FoodForm, extra=len(sweetsList))
    formset=sweetsFormset(request.POST or None)
    formzip=zip(formset, sweetsList)
    last=len(formset)
    for form in formset.forms:
        if form.is_valid():
            freq=form.cleaned_data['food_freq']
            new_data=FoodData(user=user_object, food_freq=freq, food_name=sweetsList[i])
            i=i+1
            new_data.save()
            if i==last:
                return HttpResponseRedirect('beverages')
    context ={"formset": formset, "sweetsList": sweetsList, "formzip":formzip, "freq_options": freq_options,}
    template = "sweets.html"
    return render(request,template,context)
def genq2(request):
    context ={}
    template = ""
    return HttpResponse("Final general questions go here")
