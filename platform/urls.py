from snippets import views
from django.conf.urls import patterns, url, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'persons', views.PersonViewSet)

urlpatterns = patterns('',
    url(r'^', include(router.urls)),
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)
