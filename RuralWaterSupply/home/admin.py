from django.contrib import admin
from .models import *
# Register your models here.
m=[BigProject,Project,Request,LargeScale,SmallScale,Village,Notice,Organization,Appointment,OrganizationContact,LocalPersonnel,Community]
admin.site.register(m)