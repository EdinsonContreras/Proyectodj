from django import forms  
from smartw.models import Smartband  
class SmartbandForm(forms.ModelForm):  
    class Meta:  
        model = Smartband 
        fields = "__all__"  