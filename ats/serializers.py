from rest_framework import serializers
from ats.models import *
from django.contrib.auth.models import User

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username',)

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        # fields = ('url', 'first_name','last_name','email','username',)
        fields = '__all__'

class OrganizationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Organization
        fields = '__all__'

class RoleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'

class UserProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('url', 'user','organization')

class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    # my_field = serializers.SerializerMethodField('is_active')

    # def is_active(self, project):
    #     userProfiles = UserProfile.objects.filter(organization=project.organization)
    #     return UserProfileSerializer(userProfiles, many=True, context={'request': request}).data
    
    class Meta:
        model = Project
        fields = ('url', 'created','organization','role','status','openPositionsCount','filledPositionsCount')#,'my_field')



