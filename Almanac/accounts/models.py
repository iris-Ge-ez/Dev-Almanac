from django.db import models
from django.contrib.auth.models import AbstractUser
from ckeditor.fields import RichTextField
from taggit.managers import TaggableManager

SEX = [
	('M', 'Male'),
	('F', 'Female')
]

class CustomUser(AbstractUser):
	sex = models.CharField(max_length=2, choices=SEX, default='M')
	bio = RichTextField()
	pp = models.ImageField(upload_to='Profile Pictures')
	skills = TaggableManager()

	def __str__(self):
		return self.username

