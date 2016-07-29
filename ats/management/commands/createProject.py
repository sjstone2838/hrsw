import datetime

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

from pydash import py_

# TODO: import each model individually
from ats.models import *


class Command(BaseCommand):
    help = """python manage.py createProject [userCount] \n This creates a new
    project, mapped to a new role and new organization, with [userCount] new
    users from that organization."""

    def add_arguments(self, parser):
        parser.add_argument('userCount', nargs='+', type=int)
        # parser.add_argument('applicantCount', nargs='+', type=int)

    def create_org(self):
        self.companySecondSyllables = ['Systems', 'Technologies', 'Group',
                                       'Capital',
                                       'Partners', 'Holdings', 'Industries',
                                       'Productions', 'Studios',
                                       'Construction']
        self.companyFirstSyllables = ['Aero', 'Budget', 'Sys', 'Macro',
                                      'Micro', 'Alpha', 'Beta', 'A', 'Bio',
                                      'Vertex', 'Dyno', 'Mega']

        self.organization = Organization.objects.create(
            # can also use random.sample() or random.choice()
            name=py_.sample(self.companyFirstSyllables) + '-' +
            py_.sample(self.companySecondSyllables),
            industry=py_.sample(ORGANIZATION_INDUSTRY_CHOICES)[1]
        )

    def create_role(self):
        self.roleTitles = ['Analyst', 'Engineer',
                           'Rep', 'CEO', 'CFO', 'Cashier', 'Driver']

        self.role = Role.objects.create(
            organization=self.organization,
            title=py_.sample(self.roleTitles),
            description='Lorum Ipsum Dolorum'
        )

    def createProject(self):
        self.project = Project.objects.create(
            organization=self.organization,
            role=self.role,
            status=py_.sample(PROJECT_STATUS_CHOICES)[1],
            openPositionsCount=py_.random(1, 10)
        )

    def createUser(self):
        self.userFirstNames = ['Allen', 'Bob', 'Chris', 'Dan', 'Ed', 'Fred',
                               'John', 'Tim',
                               'Sam', 'Mark', 'David', 'Colin', 'Sue', 'Jen',
                               'Emily', 'Ali', 'Brett', 'Laura', 'Joan']
        self.userLastNames = ['Smith', 'Brown', 'White', 'Case', 'Wood',
                              'Spitzer', 'Cohen', 'Hull',
                              'Liu', 'Stone', 'Swenson', 'Bunn', 'Gross',
                              'Johnson', 'Andrews', 'Harte', 'Lindsay']

        first = py_.sample(self.userFirstNames)
        last = py_.sample(self.userLastNames) + '-' + \
            py_.sample(self.userLastNames)

        user = User.objects.create(
            first_name=first,
            last_name=last,
            email=(first + '.' + last + '@test.com').lower(),
            username=(first + '_' + last).lower(),
        )
        user.set_password(self.organization.name)
        user.save()

        userProfile = UserProfile.objects.create(
            user=user,
            organization=self.organization
        )

        print 'Created user: ' + str(user)
        return userProfile

    def create_applicant_event(self, applicant, owner):
        print str(applicant)
        print str(owner)

        applicantEvent = ApplicantEvent.objects.create(
            applicant=applicant,
            eventType=py_.sample(APPLICANTEVENT_EVENTTYPE_CHOICES)[1],
            datetime=datetime.datetime.now(),
            owner=owner
        )

    def create_applicant(self):
        self.applicantFirstNames = ['Aarav', 'Aarush', 'Aayush', 'Advik',
                                    'Akarsh', 'Arnav', 'Aniruddh', 'Bhavin',
                                    'Chirag', 'Darshit', 'Devansh',
                                    'Dhruv', 'Divit', 'Divyansh', 'Eshan',
                                    'Faiyaz', 'Gurkiran', 'Hansh', 'Harikiran', 'Himmat', 'Hiran', 'Indrajit', 'Indranil',
                                    'Jayesh', 'Kiaan', 'Lakshit', 'Lakshay',
                                    'Madhup', 'Mitul', 'Neerav', 'Nishith',
                                    'Ojas', 'Pranay', 'Priyansh', 'Rachit',
                                    'Reyansh', 'Ranbir', 'Rohan', 'Sahil',
                                    'Samar',
                                    'Shaan', 'Shlok', 'Shray', 'Shreyas',
                                    'Tushar', 'Uthkarsh', 'Vaibhav', 'Vihaan', 'Vivaan', 'Yakshit']
        self.applicantLastNames = ['Bawa', 'Bedi', 'Beharry', 'Behl', 'Ben',
                                   'Bera', 'Bhagat', 'Bhakta', 'Bhalla',
                                   'Bhandari', 'Bhardwaj', 'Bhargava',
                                   'Bhasin', 'Bhat', 'Bhatia', 'Bhatnagar',
                                   'Bhatt', 'Bhattacharyya', 'Bhatti', 'Bhavsar', 'Bir', 'Biswas', 'Boase', 'Bobal',
                                   'Bora', 'Borah', 'Borde', 'Borra', 'Bose',
                                   'Brahmbhatt', 'Brar', 'Buch', 'Bumb',
                                   'Butala', 'Chacko',
                                   'Chad', 'Chada', 'Chadha', 'Chahal',
                                   'Chakrabarti',
                                   'Chakraborty', 'Chana', 'Chand', 'Chanda',
                                   'Chander',
                                   'Chandra', 'Chandran', 'Char', 'Chatterjee',
                                   'Chaudhari']

        first = py_.sample(self.applicantFirstNames)
        last = py_.sample(self.applicantLastNames) + '-' + \
            py_.sample(self.applicantLastNames)

        person = Person.objects.create(
            first_name=first,
            last_name=last,
            email=(first + '.' + last + '@test.com').lower()
        )

        applicant = Applicant.objects.create(
            person=person,
            project=self.project
        )

        print 'Created applicant: ' + str(applicant)
        return applicant

    def handle(self, *args, **options):
        user_count = options['userCount'][0]

        self.create_org()
        self.create_role()
        self.createProject()
        for x in range(0, user_count):
            owner = self.createUser()
            applicant = self.createApplicant()
            self.create_applicant_event(applicant, owner)
