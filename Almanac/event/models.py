from statistics import mode
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class Event(models.Model):
    class Types(models.TextChoices):
        HACKATHON = "HACKATHON", "Hackathon"
        SKILL_SHARING = "SKILL_SHARING", "SkillSharing"
        PRODUCTS = "PRODUCTS", "Products"
        ANNOUNCEMENTS = "ANNOUNCEMENTS", "Announcements"

    base_type = Types.SKILL_SHARING
    type = models.CharField(_("Type"), max_length=255, choices=Types.choices)



    # def get_absolute_url(self):
    #     return reverse("event_detail", kwargs={"pk": self.pk})


    def save(self, *args, **kwargs):
        if not self.id:
            self.type = self.base_type
        return super().save(*args, **kwargs)



class HackathonManager(models.Manager):
	def get_queryset(self, *args, **kwargs):
		return super().get_queryset(*args, **kwargs).filter(type=Event.Types.HACKATHON)

class SkillSharingManager(models.Manager):
	def get_queryset(self, *args, **kwargs):
		return super().get_queryset(*args, **kwargs).filter(type=Event.Types.SKILL_SHARING)

class ProductsManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=Event.Types.PRODUCTS)

class AnnouncementsManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=Event.Types.ANNOUNCEMENTS)


class HackathonMore(models.Model):
    hackathon = models.OneToOneField(Event, on_delete=models.CASCADE)



class Hackathon(Event):
	base_type = Event.Types.HACKATHON
	objects = HackathonManager

	class Meta:
		proxy = True



class SkillSharingMore(models.Model):
	skill_sharing = models.OneToOneField(Event, on_delete=models.CASCADE)


class SkillSharing(Event):
	base_type = Event.Types.SKILL_SHARING
	objects = SkillSharingManager

	# @property
	# def more(self):
	# 	return self.SkillSharingMore
	

	class Meta:
		proxy = True


class ProductsMore(models.Model):
    products = models.OneToOneField(Event, on_delete=models.CASCADE)


class Products(Event):
    base_type = Event.Types.PRODUCTS

    class Meta:
        proxy = True


class AnnouncementsMore(models.Model):
    Announcements = models.OneToOneField(Event, on_delete=models.CASCADE)
    
class Announcements(Event):
    base_type = Event.Types.ANNOUNCEMENTS

    class Meta:
        proxy = True