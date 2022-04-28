from django import forms
from Accounts.models import CustomUser

class CustomUserRegitrationForm(forms.Form):
	class Meta:
		model = CustomUser
		fields = ('username', 'first_name', 'last_name', 'email', 'sex', 'bio', 'pp', 'skills')
