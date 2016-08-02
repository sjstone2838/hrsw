from django.contrib import admin
from .models import UserProfile, Organization, Role, Person, Question, Applicant, ApplicantEvent, Project
# from django.core import urlresolvers
# from django.http import HttpResponse

def standard_fields(model):
    fields = []
    for field in model._meta.fields:
        if field.get_internal_type() != "ManyToManyField":
            fields.append(field.name)
    return tuple(fields)

class OrganizationAdmin(admin.ModelAdmin):
    list_display = standard_fields(Organization)
    list_display_links = list_display
admin.site.register(Organization, OrganizationAdmin)

class ProjectAdmin(admin.ModelAdmin):
    list_display = standard_fields(Project)
    list_display_links = list_display
    list_filter = ('organization',)
admin.site.register(Project, ProjectAdmin)

class RoleAdmin(admin.ModelAdmin):
    list_display = standard_fields(Role)
    list_display_links = list_display
admin.site.register(Role, RoleAdmin)

class UserProfileAdmin(admin.ModelAdmin):
    list_display = standard_fields(UserProfile)
    list_display_links = list_display
admin.site.register(UserProfile, UserProfileAdmin)

class PersonAdmin(admin.ModelAdmin):
    list_display = standard_fields(Person)
    list_display_links = list_display
admin.site.register(Person, PersonAdmin)

class ApplicantAdmin(admin.ModelAdmin):
    list_display = standard_fields(Applicant)
    list_display_links = list_display
admin.site.register(Applicant, ApplicantAdmin)

class ApplicantEventAdmin(admin.ModelAdmin):
    list_display = standard_fields(ApplicantEvent)
    list_display_links = list_display
admin.site.register(ApplicantEvent, ApplicantEventAdmin)

class QuestionAdmin(admin.ModelAdmin):
    list_display = standard_fields(Question)
    list_display_links = list_display
admin.site.register(Question, QuestionAdmin)
