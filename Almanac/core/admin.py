from django.contrib import admin
from core.models import *

# register models
admin.site.register((Event, Hackathon, HackathonMore, SkillSharing, SkillSharingMore, Products, ProductsMore, Announcements))

