from django import forms
from .models import User, VitaminData


stuff=(
    ('LO','Less than 10,000 IU'),
    ('UK','Do not know'),
)
VitBoolChoice=(
    ('NO', 'No'),
    ('YES_S','Yes, seasonal only'),
    ('YES_A', 'Yes, most months'),
)
#Make Form for User Identification
class UserIDForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['Identification_Number','Please_repeat_Identification_Number']


#Make form for input of Vitamin Data        
class VitaminForm(forms.ModelForm):
    vitamin_Boolean=forms.ChoiceField(choices=VitBoolChoice, widget=forms.RadioSelect, help_text='If Yes,')
    vitamin_Amount=forms.ChoiceField(choices=stuff)
    class Meta:
        model = VitaminData
        fields = ['vitamin_Boolean', 'vitamin_Amount', 'vitamin_Name']

#    vitamin_Name="Vitamin A"
#    vitamin_Boolean=forms.IntegerField()
 #   vitamin_Amount=forms.ChoiceField(choices=stuff)
    
    
    