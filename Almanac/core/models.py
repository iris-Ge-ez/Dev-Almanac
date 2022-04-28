import imp
from unicodedata import name
from django.db import models
from ckeditor.fields import RichTextField
from django.forms import CharField
from taggit.managers import TaggableManager
from accounts.models import CustomUser
import uuid

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