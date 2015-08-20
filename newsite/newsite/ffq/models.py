from django.db import models


# Create your models here.
class User(models.Model):
    Identification_Number=models.IntegerField(default=0)
    Please_repeat_Identification_Number=models.CharField(max_length=200, default ="", primary_key=True)
    timestamp = models.DateTimeField(auto_now_add = True, auto_now=False)
    def __unicode__(self):
        return self.Please_repeat_Identification_Number
         
        
class QuestionData(models.Model):
    user=models.ForeignKey(User)
    field_number=models.CharField(max_length=30, primary_key=True)
    field_answer=models.CharField(max_length=100, blank=True, null=True)
    def __unicode__(self):
        return self.field_number
class VitaminData(models.Model):
    user = models.ForeignKey(User)
    vitamin_Name = models.CharField(max_length=50, blank=True, null=True)
    vitamin_Freq = models.CharField(max_length=30, blank=True, null=True)
    vitamin_Dose = models.CharField(max_length=50, blank=True, null=True)
    def __unicode__(self):
        return self.vitamin_Name
        
class FoodData(models.Model):
    user= models.ForeignKey(User)
    food_name=models.CharField(max_length=100)
    food_freq=models.CharField(max_length=50)
    food_misc=models.CharField(max_length=50, blank=True, null=True)
    def __unicode__(self):
        return self.food_name
#class Question(models.Model):
#    identify = models.ForeignKey(Identify)
#    question_text = models.CharField(max_length=200, default ="")
#    question_category = models.CharField(max_length=50, default ="")
#    def __unicode__(self):
#        return self.question_text
 
#class Choice(models.Model):
#   question = models.ForeignKey(Question)
#   choice_text=models.CharField(max_length=200)
#   value = models.IntegerField(default=0)
#   def __unicode__(self):
#       return self.choice_text
   
