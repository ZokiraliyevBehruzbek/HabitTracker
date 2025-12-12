from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Award, UserAward



@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    search_fields = ('username', 'email')

    list_filter = ('is_staff', 'is_superuser', 'is_active')

    
@admin.register(Award)
class AwardAdmin(admin.ModelAdmin):
    list_display = ('id', 'title',)
    search_fields = ('title',)
    list_filter = ()

@admin.register(UserAward)
class UserAwardAdmin(admin.ModelAdmin):
    list_display = ('user', 'award', 'awarded_at')
    search_fields = ('user__username', 'award__title')
    list_filter = ()
