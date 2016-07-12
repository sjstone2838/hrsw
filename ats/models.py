from django.db import models
from django.contrib.auth.models import User

ORGANIZATION_INDUSTRY_CHOICES = (
    ('Retail','Retail'),
    ('Software','Software'),
    ('Hardware','Hardware'),
    ('Healthcare','Healthcare'),
    ('Industrial','Industrial'),
    ('Hospitality','Hospitality')
)

class Organization(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, blank=True, default='')
    industry = models.CharField(max_length=200, choices=ORGANIZATION_INDUSTRY_CHOICES, blank=True, default='')

    def __unicode__(self):
        return self.name

class Role(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    organization = models.ForeignKey(Organization, related_name = 'Project_Organization')
    title = models.CharField(max_length=200, blank=False, default='')
    description = models.TextField(blank=True, default='')

    def __unicode__(self):
        return self.title

PROJECT_STATUS_CHOICES  = (
    ('Pre-launch','Pre-launch'),
    ('Active','Active'),
    ('Paused','Paused'),
    ('Closed','Closed')
)

class Project(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    organization = models.ForeignKey(Organization, related_name = 'Role_Organization')
    role = models.ForeignKey(Role, related_name = 'Role')
    status = models.CharField(max_length=1000, choices=PROJECT_STATUS_CHOICES, blank=True, default='')
    openPositionsCount = models.IntegerField(default = 0)
    filledPositionsCount = models.IntegerField(default = 0)


class UserProfile(models.Model):
    user = models.ForeignKey(User, related_name="UserProfile_User")
    organization = models.ForeignKey(Organization, related_name = 'UserProfile_Organization')

