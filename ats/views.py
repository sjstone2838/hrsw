from django.contrib.auth.models import User
# from django.db.models import Count

# from rest_framework import permissions
# from rest_framework import renderers
from rest_framework import viewsets
# from rest_framework.decorators import detail_route
# from rest_framework.response import Response

from .models import UserProfile, Organization, Role, Person, Question, Applicant, ApplicantEvent, Project
# from .permissions import IsOwnerOrReadOnly
from .serializers import (UserSerializer, OrganizationSerializer, RoleSerializer,
                          UserProfileSerializer, PersonSerializer, QuestionSerializer,
                          ApplicantEventSerializer, ApplicantSerializer, ProjectSerializer)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class OrganizationViewSet(viewsets.ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer

class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

class ApplicantEventViewSet(viewsets.ModelViewSet):
    queryset = ApplicantEvent.objects.all()
    serializer_class = ApplicantEventSerializer

class ApplicantViewSet(viewsets.ModelViewSet):
    queryset = Applicant.objects.all()
    serializer_class = ApplicantSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def get_queryset(self):
        queryset = Project.objects.all()

        # TODO (from Jeff Hull): modify request middleware so that it returns request.userProfile
        # (search 'custom Django request middleware')
        if not self.request.user.is_superuser:
            user_profile = UserProfile.objects.get(user=self.request.user)
            queryset = queryset.filter(organization=user_profile.organization)

        return queryset

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
