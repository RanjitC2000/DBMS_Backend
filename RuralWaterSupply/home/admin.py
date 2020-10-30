from django.contrib import admin
from .models import *
# Register your models here.
m=[BigProject,Request,LargeScale,SmallScale,Village,Organization,Appointment,OrganizationContact,LocalPersonnel]
admin.site.register(m)