from django import forms 
from home.models import *
  
class CommunityForm(forms.ModelForm): 
  
    class Meta: 
        model = Community
        fields = ['title','subject','body','thumb']

class PublishForm(forms.ModelForm): 
  
    class Meta: 
        model = Notice
        fields = ['FirstName','LastName','Title','Body']

class StatusForm(forms.ModelForm): 
  
    class Meta: 
        model = Request
        fields = ['username','Project_ID']

        