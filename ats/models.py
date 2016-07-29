from django.db import models
from django.contrib.auth.models import User

# TODO generally python PEP8 says use snake_case
# Variables and functions are also  snake_case
# FILENAMES are also snake_case

ORGANIZATION_INDUSTRY_CHOICES = (
    ('Retail', 'Retail'),
    ('Software', 'Software'),
    ('Hardware', 'Hardware'),
    ('Healthcare', 'Healthcare'),
    ('Industrial', 'Industrial'),
    ('Hospitality', 'Hospitality')
)


class Organization(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, blank=True, default='', unique=True)
    industry = models.CharField(max_length=200,
                                choices=ORGANIZATION_INDUSTRY_CHOICES,
                                blank=True,
                                default='')

    def __unicode__(self):
        return self.name

class Role(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    organization = models.ForeignKey(Organization, related_name='Role_Organization')
    title = models.CharField(max_length=200, blank=False, default='')
    description = models.TextField(blank=True, default='')

    def __unicode__(self):
        return self.title

PROJECT_STATUS_CHOICES = (
    ('Pre-launch', 'Pre-launch'),
    ('Active', 'Active'),
    ('Paused', 'Paused'),
    ('Closed', 'Closed')
)

class Project(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    organization = models.ForeignKey(Organization, related_name='Project_Organization')
    role = models.ForeignKey(Role, related_name='Role')
    status = models.CharField(max_length=1000, choices=PROJECT_STATUS_CHOICES, blank=True, default='')
    openPositionsCount = models.IntegerField(default=0)
    filledPositionsCount = models.IntegerField(default=0)

    def __unicode__(self):
        return self.role.title + ' at ' + self.organization.name

class UserProfile(models.Model):
    # Should be OneToOneField
    user = models.ForeignKey(User, related_name="UserProfile_User")
    organization = models.ForeignKey(Organization, related_name='UserProfile_Organization')

    def __unicode__(self):
        return "{} {} ({})".format(
            self.user.first_name,
            self.user.last_name,
            self.organization.name)

class Person(models.Model):
    first_name = models.CharField(max_length=200, blank=False)
    last_name = models.CharField(max_length=200, blank=False)
    email = models.EmailField(max_length=200, blank=False, unique=True)

    def __unicode__(self):
        return self.first_name + ' ' + self.last_name

class Applicant(models.Model):
    person = models.ForeignKey(Person, blank=False)
    project = models.ForeignKey(Project, related_name="applicants", blank=False)

    def __unicode__(self):
        return (self.person.first_name + ' ' +
                self.person.last_name + ': ' +
                self.project.role.title + ' at ' +
                self.project.organization.name)

APPLICANTEVENT_EVENTTYPE_CHOICES = (
    ('Interview', 'Interview'),
    ('Resume_submission', 'Resume_submission')
)

class ApplicantEvent(models.Model):
    applicant = models.ForeignKey(Applicant, blank=False, related_name='applicantEvents')
    eventType = models.CharField(max_length=200, choices=APPLICANTEVENT_EVENTTYPE_CHOICES, blank=False)
    datetime = models.DateTimeField(blank=True)
    owner = models.ForeignKey(UserProfile, blank=True)

    def __unicode__(self):
        return str(self.applicant) + ": " + self.eventType

class Question(models.Model):
    question = models.TextField(blank=True, default='')
    answer = models.CharField(max_length=200, blank=True, null=True)
    index = models.IntegerField(default=0)
    role = models.ForeignKey(Role, blank=True, null=True, related_name='questions')
    project = models.ForeignKey(Project, blank=True, null=True, related_name='questions')
    applicantEvent = models.ForeignKey(ApplicantEvent, blank=True, null=True, related_name='questions')

    def __unicode__(self):
        return self.question[0:100]
