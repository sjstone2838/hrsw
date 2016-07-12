from django.core.management.base import BaseCommand
from ats.models import *
from sys import argv
import pydash
from pydash import py_ 

class Command(BaseCommand):
	args = '<foo bar ...>'
	help = 'python manage.py createProject [numberOfUsers] \n This creates a new project, mapped to a new role and new organization, with [numberOfUsers] new users from that organization. Default newUsers is 1'

	def createOrg(self):
		self.companySecondSyllables = ['Systems','Technologies','Group','Capital','Partners','Holdings','Industries','Productions','Studios','Construction']
		self.companyFirstSyllables = ['Aero', 'Budget','Sys', 'Macro', 'Micro','Alpha','Beta','A','Bio','Vertex','Dyno','Mega']
		
		self.organization = Organization.objects.create(
			name = py_.sample(self.companyFirstSyllables) + '-' + py_.sample(self.companySecondSyllables),
			industry = py_.sample(ORGANIZATION_INDUSTRY_CHOICES)[1]
		)

	def createRole(self):
		self.roleTitles = ['Analyst','Engineer','Rep','CEO','CFO','Cashier','Driver']
		
		self.role = Role.objects.create(
			organization = self.organization,
	    title = py_.sample(self.roleTitles),
	    description = 'Lorum Ipsum Dolorum'
		)

	def createProject(self):
		self.project = Project.objects.create(
    	organization = self.organization,
    	role = self.role,
    	status = py_.sample(PROJECT_STATUS_CHOICES)[1],
    	openPositionsCount = py_.random(1,10)
		)

	def createUser(self):
		self.firstNames = ['Allen','Bob','Chris','Dan','Ed','Fred','John','Tim','Sam','Mark','David','Colin','Sue','Jen','Emily','Ali','Brett','Laura','Joan']
		self.lastNames = ['Smith','Brown','White','Case','Wood','Spitzer','Cohen','Hull','Liu','Stone','Swenson','Bunn','Gross','Johnson','Andrews','Harte','Lindsay']

		first = py_.sample(self.firstNames)
		last = py_.sample(self.lastNames) + '-' + py_.sample(self.lastNames)
		
		user = User.objects.create(
			first_name = first,
			last_name = last,
			email = (first + '.' + last + '@test.com').lower(),
			username = (first + '_' + last).lower(),
		)
		user.set_password(self.organization.name)
		user.save()

		UserProfile.objects.create(
			user = user,
			organization = self.organization
		)

		print user
		print self.organization

	def handle(self, *args, **options):
		userCount = 1

		if len(argv) > 2:
			userCount = int(argv[2])

		self.createOrg()
		self.createRole()
		self.createProject()
		for x in range(0, userCount):
			self.createUser()
