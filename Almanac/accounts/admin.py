from django.contrib import admin
from accounts.models import CustomUser

class CustomUserAdminManager(admin.ModelAdmin):
	readonly_fields = ['password']
	list_display = ('username', 'first_name', 'last_name', 'is_superuser')
	fieldsets = (
		('Personal Informations', {
			'fields': ('username', 
					'first_name', 
					'last_name', 
					'email', 
					'sex', 
					'bio', 
					'pp', 
					'skills', 
					'password', 
					'date_joined')
			}),
		('Advanced Options', {
			'fields': ('user_permissions', 'groups', 'is_staff', 'is_active', 'is_superuser')
			}),
		)

admin.site.register(CustomUser, CustomUserAdminManager)
