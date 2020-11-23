from django.contrib import admin
from core import models

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'name', 'is_staff',)
    list_filter = ('is_staff',)
    search_fields = ('email',)
    list_per_page = 50
    

class CarAdmin(admin.ModelAdmin):
    list_display = ('user_profile', 'car_type', 'Yuk_Ulaglar', 'Yorute_Tehnikalar')

class CityAdmin(admin.ModelAdmin):
    list_display = ('Welayat', 'Etrap')
    list_filter = ('Welayat',)

admin.site.register(models.UserProfile, UserAdmin)
admin.site.register(models.Welayat)
admin.site.register(models.Tasks)
admin.site.register(models.Car, CarAdmin)
admin.site.register(models.YukUlaglar)
admin.site.register(models.TehnikiUlaglar)
admin.site.register(models.City,CityAdmin)