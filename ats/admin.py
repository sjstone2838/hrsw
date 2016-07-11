from django.contrib import admin
from snippets.models import *
from .models import *
from django.core import urlresolvers
from django.http import HttpResponse

class SnippetAdmin(admin.ModelAdmin):
  list_display = ('created', 'title', 'code',  'linenos',  'language', 'style', 'owner', 'highlighted')

admin.site.register(Snippet,SnippetAdmin)

class PersonAdmin(admin.ModelAdmin):
  list_display = ('pk','first_name', 'last_name', 'created')

admin.site.register(Person,PersonAdmin)

class OrganizationAdmin(admin.ModelAdmin):
  list_display = ('pk','name', 'industry')

admin.site.register(Organization,OrganizationAdmin)