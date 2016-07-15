from rest_framework import serializers
from ats.models import *
from django.contrib.auth.models import User

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url','username','first_name','last_name','email')

class OrganizationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Organization
        fields = '__all__'

class RoleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'

class UserProfileSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer()
    organization = OrganizationSerializer()

    class Meta:
        model = UserProfile
        fields = '__all__'

class PersonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'

class ApplicantEventSerializer(serializers.HyperlinkedModelSerializer):
    # owner = UserProfileSerializer()

    class Meta:
        model = ApplicantEvent
        fields = ('url','applicant','eventType','datetime','owner')

class ApplicantSerializer(serializers.HyperlinkedModelSerializer):
    
    # person is a related object of applicant
    person = PersonSerializer()
    applicantEvents = ApplicantEventSerializer(many=True)

    class Meta:
        model = Applicant
        depth = 3
        # applicant is a reverse relation; this tracks to the related_name of models.ApplicantEvent.applicant
        fields = ('url','person','project','applicantEvents')

class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    
    organization = OrganizationSerializer()
    applicants = ApplicantSerializer(many=True)

    class Meta:
        model = Project
        depth = 3
        fields = ('url', 'created','organization','role','status','openPositionsCount','filledPositionsCount','applicants')



