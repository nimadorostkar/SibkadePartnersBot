from django.apps import AppConfig
from django.core.management import call_command

class OrderConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'order'

    def ready(self):
        call_command('schedule_tasks')

