from django import forms
from .models import User, VitaminData, FoodData
from django.forms.widgets import RadioFieldRenderer, CheckboxFieldRenderer
from django.utils.encoding import force_unicode
from django.utils.safestring import mark_safe

stuff=(
    ('0','LOW'),
    ('1','MED-LOW'),
    ('2','MED-HIGH'),
    ('3', 'HIGH'),
    ('4', 'DK'),
)
VitBoolChoice=(
    ('0', 'No'),
    ('1','Yes, seasonal only'),
    ('2', 'Yes, most months'),
)
VitAChoices=["Less than 10,000 IU","10,000 to 15,000 IU", "16,000 to 22,000 IU", "23,000 IU or more", "Don't Know"]
PotaChoices=["Less than 2.5 mEq (100mg)","3 to 10 mEq", "11 to 20 mEq", "21 mEq or more", "Don't Know"]
VitCChoices=["Less than 400 mg", "400 to 700 mg", "750 to 1250 mg", "1300 mg or more", "Don't Know"]
VitBChoices=["Less than 50 mg", "50 to 99 mg", "100 to 149 mg", "150 mg or more", "Don't know"]
VitEChoices=["Less than 100 IU", "100 to 250 IU", "300 to 500 IU", "600 IU or more", "Don't Know"]
CalcChoices=["Less than 600 mg", "600 to 900 mg", "901 to 1500 mg", "1501 mg or more", "Don't Know"]
SeleChoices=["Less than 80 mcg", "80 to 130 mcg", "140 to 250 mcg", "260 mcg or more", "Don't Know"]
VitDChoices=["Less than 300 IU", "300 to 500 IU", "600 to 900 IU", "1000 IU or more", "Don't Know"]
ZincChoices=["Less than 25 mg", "25 to 74 mg", "75 to 100 mg", "101 mg or more", "Don't Know"]
VitTotalChoices=[VitAChoices, PotaChoices, VitCChoices, VitBChoices, VitEChoices, CalcChoices, SeleChoices, VitDChoices, ZincChoices]
frequencies=(
    ('0','Never, or less than once per month'),
    ('1','1-3 per month'),
    ('2','1 per week'),
    ('3','2-4 per week'),
    ('4','5-6 per week'),
    ('5','1 per day'),
    ('6','2-3 per day'),
    ('7','4-5 per day'),
    ('8','6+ per day'),

)
BoolChoice=(
    ('0', 'No'),
    ('1', 'Yes')
)
MultiChoice=(
    ('0','2 or less'),
    ('1','3-5'),
    ('2','6-9'),
    ('3','10 or more'),
)
MultiBrands=(
    ('0','Centrum Silver'),
    ('1','Centrum'),
    ('2','Theregran M'),
    ('3','One-A-Day Essential'),
    ('4','Other:'),
    
)
MilkChoices=(
    ('0', 'Whole Milk'),
    ('1', '2%% Milk'),
    ('2', 'Skim Milk'),
    ('3', 'Almond Milk'),
    ('4', 'Soy Milk'),
    ('5', 'None'),
    ('6', 'Other'),
)
MilkAmounts=(
    ('0', 'None'),
    ('1', '1/2 cup'),
    ('2', '1 cup'),
    ('3', '1.5 cups'),
    ('4', '2 cups'),
    ('5', 'More than 2 cups'),
)
FatChoices=(
    ('0', 'None'),
    ('1', 'Butter'),
    ('2', 'Lard/Dripping'),
    ('3', 'Vegetable Oil'),
    ('4', 'Solid vegetable fat'),
    ('5', 'Margarine'),
)
FriedChoices=(
    ('0','Never'),
    ('1','Less than once per week'),
    ('2','1-3 times per week'),
    ('3','4-6 times per week'),
    ('4', 'Daily')
)
MeatChoices=(
    ('0','Did not eat meat'),
    ('1','Lightly cooked/rare'),
    ('2','Medium'),
    ('3','Well done /dark brown'),
)
SaltChoices=(
    ('0','Never'),
    ('1','Rarely'),
    ('2','Sometimes'),
    ('3','Usually'),
    ('4','Always'),
)

class MyCustomRenderer( RadioFieldRenderer ):
    def render( self ):
        """Outputs a series of <td></td> fields for this set of radio fields."""
        return( mark_safe( u''.join( [ u'<td>%s</td>' % force_unicode(w.tag()) for w in self ] )))
        
class MyCustomRendererWithLabel( RadioFieldRenderer ):
    def render( self ):
        """Outputs a series of <td></td> fields for this set of radio fields."""
        for w in self:
            print(w)
        return( mark_safe( u''.join( [ u'<td>%s</td>' % force_unicode(w) for w in self ] )))   

class CheckboxRendererWithLabel( CheckboxFieldRenderer ):
    def render( self ):
        """Outputs a series of <td></td> fields for this set of radio fields."""
        for w in self:
            print(w)
        return( mark_safe( u''.join( [ u'<td>%s</td>' % force_unicode(w) for w in self ] )))     
        
#Make Form for User Identification
class UserIDForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['Identification_Number','Please_repeat_Identification_Number']


#Make form for input of Vitamin Data        
class VitaminForm(forms.Form):
    vitamin_Boolean=forms.ChoiceField(choices=VitBoolChoice, widget=forms.RadioSelect, help_text='If Yes,')
    vitamin_Amount=forms.ChoiceField(choices=stuff, widget = forms. RadioSelect(renderer=MyCustomRenderer),required=False)
    
class FoodForm(forms.Form):
    food_freq=forms.ChoiceField(choices=frequencies, widget=forms.RadioSelect(renderer=MyCustomRenderer))
    #food_misc=forms.ChoiceField(choices)
    
class MultiForm(forms.Form):
    multi_boolean=forms.ChoiceField(choices=BoolChoice, widget=forms.RadioSelect, help_text='If Yes,')
    multi_freq=forms.ChoiceField(choices=MultiChoice, widget=forms.RadioSelect(renderer=MyCustomRendererWithLabel), required=False)
    multi_brand=forms.ChoiceField(choices=MultiBrands, widget=forms.CheckboxSelectMultiple(renderer=CheckboxRendererWithLabel), required=False)
    multi_other=forms.CharField(required=False)
    
class BackForm(forms.Form):
    other_bool=forms.ChoiceField(choices=BoolChoice, widget=forms.CheckboxSelectMultiple(renderer=CheckboxRendererWithLabel))
    milk_type=forms.ChoiceField(choices=MilkChoices, widget=forms.RadioSelect(renderer=MyCustomRendererWithLabel))
    milk_amount=forms.ChoiceField(choices=MilkAmounts, widget=forms.RadioSelect(renderer=MyCustomRendererWithLabel))
    cereal_bool=forms.ChoiceField(choices=BoolChoice, widget=forms.RadioSelect(renderer=MyCustomRendererWithLabel))
    cereal_brand1=forms.CharField(required=False)
    cereal_type1=forms.CharField(required=False)
    cereal_brand2=forms.CharField(required=False)
    cereal_type2=forms.CharField(required=False)
    fat_fry=forms.ChoiceField(choices=FatChoices, widget=forms.RadioSelect(renderer=MyCustomRendererWithLabel))
    fat_fry_type=forms.CharField(required=False)
    fat_bake=forms.ChoiceField(choices=FatChoices, widget=forms.RadioSelect(renderer=MyCustomRendererWithLabel))
    fat_bake_type=forms.CharField(required=False)
    fried_home=forms.ChoiceField(choices=FriedChoices, widget=forms.RadioSelect(renderer=MyCustomRendererWithLabel))
    fried_away=forms.ChoiceField(choices=FriedChoices, widget=forms.RadioSelect(renderer=MyCustomRendererWithLabel))
    meat_freq=forms.IntegerField(help_text='times a week')
    meat_level=forms.ChoiceField(choices=MeatChoices, widget=forms.RadioSelect(renderer=MyCustomRendererWithLabel))
    salt_cooking=forms.ChoiceField(choices=SaltChoices, widget=forms.RadioSelect(renderer=MyCustomRendererWithLabel))
    salt_eating=forms.ChoiceField(choices=SaltChoices, widget=forms.RadioSelect(renderer=MyCustomRendererWithLabel))
    fake_salt=forms.ChoiceField(choices=BoolChoice, widget=forms.RadioSelect(renderer=MyCustomRendererWithLabel))
    fake_salt_type=forms.CharField(required=False)
    
    
    
    
    
    

#    vitamin_Name="Vitamin A"
#    vitamin_Boolean=forms.IntegerField()
 #   vitamin_Amount=forms.ChoiceField(choices=stuff)
    
    
    