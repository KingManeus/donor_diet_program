from django.contrib import admin

from .models import User, VitaminData, FoodData



class VitaminDataInline(admin.TabularInline):
    model = VitaminData
    extra = 0
    
class FoodDataInline(admin.TabularInline):
    model = FoodData
    extra = 0

class UserAdmin(admin.ModelAdmin):
    inlines = [VitaminDataInline, FoodDataInline]
    
admin.site.register(User,UserAdmin)

