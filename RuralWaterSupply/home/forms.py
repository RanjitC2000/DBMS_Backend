from django import forms 
from .models import *
  
class CommunityForm(forms.ModelForm): 
  
    class Meta: 
        model = Community
        fields = ['title','subject','body','thumb']
        
class StatusForm(forms.ModelForm): 
  
    class Meta: 
        model = Request
        fields = ['username','Project_ID']

class ProjectForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = ['Project_Type','Project_Scale']

class AppointmentForm(forms.ModelForm):

    class Meta:
        model = Appointment
        fields = ['username','Personnel_ID','TimeSlot']
