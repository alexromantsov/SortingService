from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = 'Create default users'

    def create_superuser(self):
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', 'admin@example.com', 'uG7#2$k9')
            print("   >>> Суперпользователь admin - создан!")
        else:
            print("   >>> Суперпользователь admin уже существует")

    def handle(self, *args, **kwargs):
        self.create_superuser()
