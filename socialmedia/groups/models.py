from django.db import models
from django.utils.text import slugify
#it puts dash(-), if we ahve any space between between text
import misaka
from django.urls import reverse
# misaka put links in your text if you want to(like a markup link).
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.
from django import template
register = template.Library()


class Group(models.Model):

    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(allow_unicode=True, unique=True)
    description = models.TextField(blank=True, default='')
    description_html = models.TextField(editable=False, default='', blank=True)
    members = models.ManyToManyField(User,through="GroupMember")

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        self.description_html = misaka.html(self.description)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("groups:single", kwargs={"slug": self.slug})

    class Meta:
        ordering = ["name"]


class GroupMember(models.Model):
    # here we create a group attribute which will be a forigin key of Group class
    group = models.ForeignKey(Group, related_name= "membership",on_delete=models.CASCADE)
    # Here we are creating user attributes which will be a ForeignKey of User class
    # which we have imported from get_user_model.
    user = models.ForeignKey(User, related_name= "user_groups", on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

    class Meta:
        unique_together = ("group", "user")
