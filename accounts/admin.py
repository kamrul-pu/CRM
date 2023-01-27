from django.contrib import admin
from accounts.models import *
# Register your models here.

class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name','phone','email']
    search_fields=['name','phone','email','date_created']

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','price','category']
    search_fields=['name','price','category']

class OrderAdmin(admin.ModelAdmin):
    list_display = ['customer','status',]
    search_fields=['customer','status',]

class TagAdmin(admin.ModelAdmin):
    list_display = ['name',]
    search_fields=['name',]

admin.site.register(Customer,CustomerAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(Order,OrderAdmin)
admin.site.register(Tag,TagAdmin)