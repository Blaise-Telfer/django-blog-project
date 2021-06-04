from django.apps import AppConfig


class AccountsConfig(AppConfig):
	name = 'project'
	
	def ready(self):
	  import project.signals

