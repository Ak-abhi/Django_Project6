from django.contrib import admin
from .models import User, UserProfile, Department
# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Department)
