from django.contrib import admin

from .models import User, VitaminData



class VitaminDataInline(admin.TabularInline):
    model = VitaminData
    extra = 0

class UserAdmin(admin.ModelAdmin):
    inlines = [VitaminDataInline]
    
admin.site.register(User,UserAdmin)

