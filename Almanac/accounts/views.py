from django.shortcuts import render
from accounts.models import CustomUser
from accounts.forms import CustomUserRegistrationForm
from django.views import View, generic
from django.http import HttpResponseRedirect

class UserRegistrationView(View):
	form_class = CustomUserRegistrationForm
	template_name = 'registration.html'

	def post(self, request, *args, **kwargs):
		form = self.form_class(request.POST)
		if form.is_valid():
			form.save(commit=False)
			form.save_m2m()

			return HttpResponseRedirect('/success/')
			
		return render(request, self.template_name, {'form': form})

class UserListView(generic.ListView):
	model = CustomUser
	context_object_name = 'developers'
	template_name = 'developers'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		return context

class UserProfileView(generic.DetailView):
	model = CustomUser
	context_object_name = 'developerdetail'
	template_name = 'devdetail.html'

	def get_object(self, **kwargs):
		self.username = self.kwargs.get('username')
		view_user = CustomUser.objects.get(username=self.username)
		return view_user

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		return context

class UserProfileUpdateView(generic.UpdateView):
	model = CustomUser
	form_class = CustomUserRegistrationForm
	template_name = 'updateprofile.html'
	success_url = '/userdetail/'

