import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE','db_exercise.settings')
django.setup()

from users.models import User
from faker import Faker

fakegen = Faker()

fname,lname = fakegen.name().split()
em = fakegen.email()

new_user = User.objects.get_or_create(first_name=fname,last_name=lname,email=em)[0]
