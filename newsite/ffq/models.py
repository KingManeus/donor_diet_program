from django.db import models


# Create your models here.
class Identify(models.Model):
    iNumber=models.IntegerField(default=0)
    iNumberRepeat=models.CharField(max_length=200, default ="")
    timestamp = models.DateTimeField(auto_now_add = True, auto_now=False)
    def __unicode__(self):
        return self.iNumberRepeat
        
class Question(models.Model):
    identify = models.ForeignKey(Identify)
    question_text = models.CharField(max_length=200, default ="")
    question_category = models.CharField(max_length=50, default ="")
    def __unicode__(self):
        return self.question_text
 
class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text=models.CharField(max_length=200)
    value = models.IntegerField(default=0)
    def __unicode__(self):
        return self.choice_text
   
