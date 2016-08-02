from django.db import models
from django.contrib.auth.models import User

class TimeStampedModel(models.Model):
    # An abstract base class model that rovides self-updating 'created' and 'modified' fields.
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


ORGANIZATION_INDUSTRY_CHOICES = (
    ('Retail', 'Retail'),
    ('Software', 'Software'),
    ('Hardware', 'Hardware'),
    ('Healthcare', 'Healthcare'),
    ('Industrial', 'Industrial'),
    ('Hospitality', 'Hospitality')
)

class Organization(TimeStampedModel):
    name = models.CharField(max_length=100, blank=True, default='', unique=True)
    industry = models.CharField(max_length=200,
                                choices=ORGANIZATION_INDUSTRY_CHOICES,
                                blank=True,
                                default='')

    def __unicode__(self):
        return self.name

class Role(TimeStampedModel):
    organization = models.ForeignKey(Organization)
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

class Project(TimeStampedModel):
    organization = models.ForeignKey(Organization)
    role = models.ForeignKey(Role)
    status = models.CharField(max_length=1000, choices=PROJECT_STATUS_CHOICES, blank=True, default='')
    open_positions_count = models.IntegerField(default=0)
    filled_positions_count = models.IntegerField(default=0)

    def __unicode__(self):
        return self.role.title + ' at ' + self.organization.name

class UserProfile(TimeStampedModel):
    user = models.OneToOneField(User, related_name='user_profile')
    organization = models.ForeignKey(Organization)

    def __unicode__(self):
        return "{} {} ({})".format(
            self.user.first_name,
            self.user.last_name,
            self.organization.name)

class Person(TimeStampedModel):
    first_name = models.CharField(max_length=200, blank=False)
    last_name = models.CharField(max_length=200, blank=False)
    email = models.EmailField(max_length=200, blank=False, unique=True)

    def __unicode__(self):
        return self.first_name + ' ' + self.last_name

class Applicant(TimeStampedModel):
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

class ApplicantEvent(TimeStampedModel):
    applicant = models.ForeignKey(Applicant, blank=False, related_name='applicant_events')
    event_type = models.CharField(max_length=200, choices=APPLICANTEVENT_EVENTTYPE_CHOICES, blank=False)
    datetime = models.DateTimeField(blank=True)
    owner = models.ForeignKey(UserProfile, blank=True)

    def __unicode__(self):
        return str(self.applicant) + ": " + self.event_type

class Question(TimeStampedModel):
    text = models.TextField(blank=True, default='')
    answer = models.CharField(max_length=200, blank=True, null=True)
    index = models.IntegerField(default=0)
    role = models.ForeignKey(Role, blank=True, null=True, related_name='questions')
    project = models.ForeignKey(Project, blank=True, null=True, related_name='questions')
    applicant_event = models.ForeignKey(ApplicantEvent, blank=True, null=True, related_name='questions')

    def __unicode__(self):
        return self.text[0:100]
