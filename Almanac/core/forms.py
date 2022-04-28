from django import forms
from core.models import Project, Hackathon, Task, Application, Enrollment

class ProjectForm(forms.Form):
	class Meta:
		model = Project
		fields = ['title', 'description', 'tags', 'requirements', 'posted_by', 'due_date']

class HackathonForm(forms.Form):
	class Meta:
		model = Hackathon
		fields = ['htitle', 'hdescription', 'htags', 'posted_by', 'go_live', 'start_date_time', 'end_date_time']

class TaskForm(forms.Form):
	class Meta:
		model = Task
		fields = ['hackathon', 'task_description']

class ApplicationForm(forms.Form):
	class Meta:
		model = Application
		fields = ['user', 'project', 'attachement']

class EnrollmentForm(forms.Form):
	class Meta:
		model = Enrollment
		fields = ['user', 'hackathon']