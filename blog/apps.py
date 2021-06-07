from django.apps import AppConfig


class AccountsConfig(AppConfig):
	name = 'blog'
	
	def ready(self):
	  import blog.signals

