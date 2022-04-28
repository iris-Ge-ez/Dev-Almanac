import imp
from unicodedata import name
from django.db import models
from ckeditor.fields import RichTextField
from django.forms import CharField
from taggit.managers import TaggableManager
from accounts.models import CustomUser
import uuid

from django_mysql.models import ListCharField

class Project(models.Model):
	title = models.CharField(max_length=120)
	description = RichTextField()
	tags = TaggableManager()
	requirements = models.FileField(upload_to='Project Requirements')
	pid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	posted_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
	posted_date = models.DateTimeField(auto_now_add=True)
	due_date = models.DateTimeField()

	def __str__(self):
		return self.title

class Application(models.Model):
	user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
	project = models.ForeignKey(Project, on_delete=models.CASCADE)
	aid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	attachement = models.FileField(upload_to='Application Attachements')
	application_date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.username + self.title

class Hackathon(models.Model):
	title = models.CharField(max_length=120)
	description = RichTextField()
	tags = TaggableManager()
	posted_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
	go_live = models.BooleanField(default=False)
	hid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	created_date = models.DateTimeField(auto_now_add=True)
	start_date_time = models.DateTimeField()
	end_date_time = models.DateTimeField()

	def __str__(self):
		return self.htitle
    

class Task(models.Model):
	hackathon = models.ForeignKey(Hackathon, on_delete=models.CASCADE)
	task_description = RichTextField()

	def __str__(self):
		return self.hackathon

class Prize(models.Model):
	hackathon = models.ForeignKey(Hackathon, on_delete=models.CASCADE)
	grand = models.IntegerField()
	# solo_ranked = ListCharField(
	# 	base_field=CharField(max_length=10),
	# 	size=6,
	# 	max_length=(6*11),
	# )

	def __str__(self) -> str:
		return super().__str__()



class Enrollment(models.Model):
	user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
	hackathon = models.ForeignKey(Hackathon, on_delete=models.CASCADE)
	eid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	enrollment_date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.username + self.htitle


