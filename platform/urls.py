from django.conf.urls import patterns, url, include
from django.contrib import admin
from django.views.generic.base import RedirectView
from rest_framework.routers import DefaultRouter

from ats import views

router = DefaultRouter()
router.register(r'applicantEvents', views.ApplicantEventViewSet)
router.register(r'applicants', views.ApplicantViewSet)
router.register(r'organizations', views.OrganizationViewSet)
router.register(r'persons', views.PersonViewSet)
router.register(r'projects', views.ProjectViewSet)
router.register(r'questions', views.QuestionViewSet)
router.register(r'roles', views.RoleViewSet)
router.register(r'userProfiles', views.UserProfileViewSet)
router.register(r'users', views.UserViewSet)

urlpatterns = patterns('',
                       url(r'^api/', include(router.urls), name='api_root'),
                       url(r'^admin/', admin.site.urls),
                       url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
                       # redirect all else to API root
                       url(r'^.*$', RedirectView.as_view(url='/api/'))
                       )
