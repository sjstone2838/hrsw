from django.contrib.auth.models import User
from django.db.models import Count

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

class RoleViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer

class UserProfileViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

class PersonViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

class ApplicantEventViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ApplicantEvent.objects.all()
    serializer_class = ApplicantEventSerializer

class ApplicantViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Applicant.objects.all()
    serializer_class = ApplicantSerializer

class ProjectViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def get_queryset(self):
        queryset = Project.objects.all()

        # TODO (from Jeff Hull): modify request middleware so that it returns request.userProfile (search 'custom Django request middleware')
        if not self.request.user.is_superuser:
            userProfile = UserProfile.objects.get(user=self.request.user)
            queryset = queryset.filter(organization=userProfile.organization)

        return queryset
