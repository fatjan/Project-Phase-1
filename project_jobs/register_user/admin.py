from django.contrib import admin
from .models import User

my_model = [User]
admin.site.register(my_model)