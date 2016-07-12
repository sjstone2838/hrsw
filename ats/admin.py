from django.contrib import admin
from ats.models import *
from .models import *
from django.core import urlresolvers
from django.http import HttpResponse

class OrganizationAdmin(admin.ModelAdmin):
  list_display = ('pk','name', 'industry','created')

admin.site.register(Organization,OrganizationAdmin)

class ProjectAdmin(admin.ModelAdmin):
  list_display = ('pk','created', 'organization', 'role', 'status', 'openPositionsCount','filledPositionsCount')

admin.site.register(Project,ProjectAdmin)

class RoleAdmin(admin.ModelAdmin):
  list_display = ('pk','title','organization','description','created')

admin.site.register(Role,RoleAdmin)

class UserProfileAdmin(admin.ModelAdmin):
  list_display = ('pk','user','organization')

admin.site.register(UserProfile,UserProfileAdmin)