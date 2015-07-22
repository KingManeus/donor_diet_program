from django import forms
from .models import User, VitaminData, FoodData
from django.forms.widgets import RadioFieldRenderer
from django.utils.encoding import force_unicode
from django.utils.safestring import mark_safe

stuff=(
    ('','-------'),
    ('LO','Less than 10,000 IU'),
    ('UK','Do not know'),
)
VitBoolChoice=(
    ('NO', 'No'),
    ('YES_S','Yes, seasonal only'),
    ('YES_A', 'Yes, most months'),
)
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

class MyCustomRenderer( RadioFieldRenderer ):
    def render( self ):
        """Outputs a series of <td></td> fields for this set of radio fields."""
        return( mark_safe( u''.join( [ u'<td>%s</td>' % force_unicode(w.tag()) for w in self ] )))
#Make Form for User Identification
class UserIDForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['Identification_Number','Please_repeat_Identification_Number']


#Make form for input of Vitamin Data        
class VitaminForm(forms.Form):
    vitamin_Boolean=forms.ChoiceField(choices=VitBoolChoice, widget=forms.RadioSelect, help_text='If Yes,')
    vitamin_Amount=forms.ChoiceField(choices=stuff, required=False)
    
class FoodForm(forms.Form):
    food_freq=forms.ChoiceField(choices=frequencies, widget=forms.RadioSelect(renderer=MyCustomRenderer))
    #food_misc=forms.ChoiceField(choices)
    


#    vitamin_Name="Vitamin A"
#    vitamin_Boolean=forms.IntegerField()
 #   vitamin_Amount=forms.ChoiceField(choices=stuff)
    
    
    