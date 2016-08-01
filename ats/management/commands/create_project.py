import datetime

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

from pydash import py_
from random import choice

from ats.models import (UserProfile, Organization, Role, Person, Applicant, ApplicantEvent, Project, Question,
                        ORGANIZATION_INDUSTRY_CHOICES, PROJECT_STATUS_CHOICES, APPLICANTEVENT_EVENTTYPE_CHOICES)


class Command(BaseCommand):
    help = """python manage.py create_project [applicant_count] [user_count]

    This creates a new project, mapped to a new role and new organization, with [applicant_count] new applicants and
    [user_count] new users from that organization. Each applicant has 1 applicantEvent and each applicantEvent has
    between 1-4 questions and answers."""

    def add_arguments(self, parser):
        parser.add_argument('applicant_count', nargs='+', type=int)
        parser.add_argument('user_count', nargs='+', type=int)

    def create_org(self):
        self.companySecondSyllables = ['Systems', 'Technologies', 'Group',
                                       'Capital',
                                       'Partners', 'Holdings', 'Industries',
                                       'Productions', 'Studios',
                                       'Construction']
        self.companyFirstSyllables = ['Aero', 'Budget', 'Sys', 'Macro',
                                      'Micro', 'Alpha', 'Beta', 'A', 'Bio',
                                      'Vertex', 'Dyno', 'Mega']

        organization = Organization.objects.create(
            # can also use random.sample() or random.choice()
            name=py_.sample(self.companyFirstSyllables) + '-' +
            py_.sample(self.companySecondSyllables),
            industry=py_.sample(ORGANIZATION_INDUSTRY_CHOICES)[1]
        )
        return organization

    def create_role(self, organization):
        role_titles = ['Analyst', 'Engineer',
                       'Rep', 'CEO', 'CFO', 'Cashier', 'Driver']

        return Role.objects.create(
            organization=organization,
            title=py_.sample(role_titles),
            description='Lorum Ipsum Dolorum'
        )

    def create_project(self, organization, role):
        return Project.objects.create(
            organization=organization,
            role=role,
            status=py_.sample(PROJECT_STATUS_CHOICES)[1],
            open_positions_count=py_.random(1, 10)
        )

    def create_user(self, organization):
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
        user.set_password(organization.name)
        user.save()

        user_profile = UserProfile.objects.create(
            user=user,
            organization=organization
        )

        return user_profile

    def create_applicant(self, project):
        self.applicantFirstNames = ['Aarav', 'Aarush', 'Aayush', 'Advik', 'Akarsh', 'Arnav', 'Aniruddh', 'Bhavin',
                                    'Chirag', 'Darshit', 'Devansh', 'Dhruv', 'Divit', 'Divyansh', 'Eshan',
                                    'Faiyaz', 'Gurkiran', 'Hansh', 'Harikiran', 'Himmat', 'Hiran', 'Indrajit',
                                    'Jayesh', 'Kiaan', 'Lakshit', 'Lakshay',
                                    'Madhup', 'Mitul', 'Neerav', 'Nishith', 'Ojas', 'Pranay', 'Priyansh', 'Rachit',
                                    'Reyansh', 'Ranbir', 'Rohan', 'Sahil',
                                    'Samar', 'Shaan', 'Shlok', 'Shray', 'Shreyas',
                                    'Tushar', 'Uthkarsh', 'Vaibhav', 'Vihaan', 'Vivaan', 'Yakshit']
        self.applicantLastNames = ['Bawa', 'Bedi', 'Beharry', 'Behl', 'Ben',
                                   'Bera', 'Bhagat', 'Bhakta', 'Bhalla', 'Bhandari', 'Bhardwaj', 'Bhargava',
                                   'Bhasin', 'Bhat', 'Bhatia', 'Bhatnagar',
                                   'Bhatt', 'Bhattacharyya', 'Bhatti', 'Bhavsar', 'Bir', 'Biswas', 'Boase', 'Bobal',
                                   'Bora', 'Borah', 'Borde', 'Borra', 'Bose', 'Brahmbhatt', 'Brar', 'Buch', 'Bumb',
                                   'Butala', 'Chacko', 'Chad', 'Chada', 'Chadha', 'Chahal', 'Chakrabarti',
                                   'Chakraborty', 'Chana', 'Chand', 'Chanda', 'Chander',
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
            project=project
        )

        return applicant

    def create_question(self, index, applicant_event):
        text_prompts = ['What\'s your favorite ', 'What\'s your least favorite ']
        text_objects = ['sport', 'resort', 'beach', 'town', 'color', 'month', 'season',
                        'state', 'country', 'airplane', 'animal', 'fish', 'job', 'brand'
                        'food', 'dessert', 'drink']

        answers = ['Ummmm...', 'That\'s a hard one...', 'I dunno...', 'Can you repeat the question?',
                   'Hot diggity!', 'Rubadubalubub!']

        text = py_.sample(text_prompts) + py_.sample(text_objects) + '?'
        answer = py_.sample(answers)

        return Question.objects.create(
            text=text,
            answer=answer,
            index=index,
            applicant_event=applicant_event
        )

    def create_applicant_event(self, applicant, owner):
        applicant_event = ApplicantEvent.objects.create(
            applicant=applicant,
            event_type=py_.sample(APPLICANTEVENT_EVENTTYPE_CHOICES)[1],
            datetime=datetime.datetime.now(),
            owner=owner
        )

        question_count = choice(range(1, 5))
        for i in range(0, question_count):
            self.create_question(i, applicant_event)

        return applicant_event

    def handle(self, *args, **options):
        organization = self.create_org()
        role = self.create_role(organization)
        project = self.create_project(organization, role)
        users = []
        applicants = []

        for x in range(0, options['user_count'][0]):
            user = self.create_user(organization)
            users.append(user)

        for x in range(0, options['applicant_count'][0]):
            applicant = self.create_applicant(project)
            self.create_applicant_event(applicant, py_.sample(users))
            applicants.append(applicant)

        print """
            Created the following project:
            Organization: {0}
            Role: {1}
            Project: {2}
            User(s): {3}
            Applicant(s): {4}
            \n
        """.format(organization, role, project, users, applicants)
