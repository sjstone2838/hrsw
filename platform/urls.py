from ats import views
from django.conf.urls import patterns, url, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'roles', views.RoleViewSet)
router.register(r'userProfiles', views.UserProfileViewSet)
router.register(r'projects', views.ProjectViewSet)
router.register(r'organizations', views.OrganizationViewSet)
router.register(r'applicants', views.ApplicantViewSet)
router.register(r'applicantEvents', views.ApplicantEventViewSet)
router.register(r'persons', views.PersonViewSet)

urlpatterns = patterns('',
    url(r'^', include(router.urls)),
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)
