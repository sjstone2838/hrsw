from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework import renderers
from rest_framework import viewsets
from rest_framework.decorators import detail_route
from rest_framework.response import Response
from ats.models import *
from ats.permissions import IsOwnerOrReadOnly
from ats.serializers import *

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class OrganizationViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer

class ProjectViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    
    def get_queryset(self):
        # TODO (from Jeff Hull): modify request middleware so that it returns request.userProfile (search 'custom Django request middleware')
        print self.request.user
        print self.request.user.is_superuser
        if not self.request.user.is_superuser:
            userProfile = UserProfile.objects.get(user=self.request.user)
            return Project.objects.filter(organization=userProfile.organization)
        return Project.objects.all()

class RoleViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer

class UserProfileViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
