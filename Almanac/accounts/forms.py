from django import forms
from accounts.models import CustomUser

class CustomUserRegistrationForm(forms.Form):
	class Meta:
		model = CustomUser
		fields = ('username', 'first_name', 'last_name', 'email', 'sex', 'bio', 'pp', 'skills')
