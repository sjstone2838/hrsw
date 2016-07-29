from django.contrib import admin
from .models import UserProfile, Organization, Role, Person, Question, Applicant, ApplicantEvent, Project
# from django.core import urlresolvers
# from django.http import HttpResponse

class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'industry', 'created')
admin.site.register(Organization, OrganizationAdmin)

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('pk', 'created', 'organization', 'role', 'status', 'openPositionsCount', 'filledPositionsCount')
admin.site.register(Project, ProjectAdmin)

class RoleAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'organization', 'description', 'created')
admin.site.register(Role, RoleAdmin)

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user', 'organization')
admin.site.register(UserProfile, UserProfileAdmin)

class PersonAdmin(admin.ModelAdmin):
    list_display = ('pk', 'first_name', 'last_name', 'email')
admin.site.register(Person, PersonAdmin)

class ApplicantAdmin(admin.ModelAdmin):
    list_display = ('pk', 'person', 'project')
admin.site.register(Applicant, ApplicantAdmin)

class ApplicantEventAdmin(admin.ModelAdmin):
    list_display = ('pk', 'applicant', 'eventType', 'datetime', 'owner')
admin.site.register(ApplicantEvent, ApplicantEventAdmin)

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('pk', 'question', 'answer', 'index', 'role', 'project', 'applicantEvent')
admin.site.register(Question, QuestionAdmin)
