from django.shortcuts import render
from django.http import HttpResponseRedirect
from core.models import Project, Hackathon, Task, Application, Enrollment
from core.forms import ProjectForm, HackathonForm, TaskForm, ApplicationForm, EnrollmentForm
from django.views import View, generic

class ProjectPostView(View):
	form_class = ProjectForm
	template_name = 'projectform.html'

	def post(self, request, *args, **kwargs):
		form = self.form_class(request.POST)

		if form.is_valid():
			form.save(commit=False)
			form.save_m2m()

			return HttpResponseRedirect('/success/')

		return render(request, self.template_name, {'form':form})

class ProjectListView(generic.ListView):
	model = Project
	context_object_name = 'projects'
	template_name = 'projectlist.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		return context

class ProjectDetailView(generic.DetailView):
	model = Project
	context_object_name = 'projectdetail'
	template_name = 'projectdetail.html'

	def get_object(self, **kwargs):
		self.pid = self.kwargs.get('pid')
		view_project = Project.objects.get(pid=self.pid)
		return view_project

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		return context

class ProjectUpdateView(generic.UpdateView):
	model = Project
	form_class = ProjectForm
	template_name = 'projectupdate.html'
	success_url = '/projectdetai/'


class HackathonPostView(View):
	form_class = HackathonForm
	template_name = 'hackathonform.html'

	def post(self, request, *args, **kwargs):
		form = self.form_class(request.POST)

		if form.is_valid():
			form.save()
			form.save_m2m()

			return HttpResponseRedirect('/success/')

		return render(request, self.template_name, {'form':form})

class HackathonListView(generic.ListView):
	model = Hackathon
	context_object_name = 'hackathons'
	template_name = 'hackathonlist.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		return context

class HackathonDetailView(generic.DetailView):
	model = Hackathon
	context_object_name = 'hackathondetail'
	template_name = 'hackathondetail.html'

	def get_object(self, **kwargs):
		self.hid = self.kwargs.get('hid')
		view_hackathon = Hackathon.objects.get(hid=self.hid)
		return view_hackathon

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		return context

class HackathonUpdateView(generic.UpdateView):
	model = Hackathon
	form_class = HackathonForm
	template_name = 'hackathonupdate.html'
	success_url = '/hackathondetail/'

class TaskPostView(View):
	form_class = TaskForm
	template_name = 'taskform.html'

	def post(self, request, *args, **kwargs):
		form = self.form_class(request.POST)

		if form.is_valid():
			form.save(commit=False)
			form.save_m2m()

			return HttpResponseRedirect('/success/')

		return render(request, self.template_name, {'form':form})

class TaskListView(generic.ListView):
	model = Task
	context_object_name = 'tasks'
	template_name = 'tasklist.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		return context

class TaskDetailView(generic.DetailView):
	model = Task
	context_object_name = 'taskdetail'
	template_name = 'taskdetail.html'

	def get_object(self, **kwargs):
		self.id = self.kwargs.get('id')
		view_task = Task.objects.get(id=self.id)
		return view_task

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		return context

class TaskUpdateView(generic.UpdateView):
	model = Task
	form_class = TaskForm
	template_name = 'taskupdate.html'
	success_url = '/taskdetail/'

class ApplicationPostView(generic.CreateView):
	model = Application
	form_class = ApplicationForm
	template_name = 'applicationform.html'
	success_url = '/applications/'

class ApplicationListView(generic.ListView):
	model = Application
	context_object_name = 'applications'
	template_name = 'applicationlist.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		return context

class ApplicationDetailView(generic.DetailView):
	model = Application
	context_object_name = 'appdetail'
	template_name = 'appdetail.html'

	def get_object(self, **kwargs):
		self.aid = self.kwargs.get('aid')
		view_application = Application.objects.get(aid=self.aid)
		return view_application

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		return context

class EnrollmentPostView(generic.CreateView):
	model = Enrollment
	form_class = EnrollmentForm
	template_name = 'enrollment.html'
	success_url = '/enrollmentlist/'

class EnrollmentListView(generic.ListView):
	model = Enrollment
	context_object_name = 'enrollments'
	template_name = 'enrollementlist'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		return context

class EnrollmentDetailView(generic.DetailView):
	model = Enrollment
	context_object_name = 'enrollmentdetail'
	template_name = 'enrolldetail.html'

	def get_object(self, **kwargs):
		self.id = self.kwargs.get('id')
		view_enroll = Enrollment.objects.get(id=self.id)
		return view_enroll

	def get_context_data(selef, **kwargs):
		context = super().get_context_data(**kwargs)
		return context


