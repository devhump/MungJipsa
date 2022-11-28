from django import forms 
from .models import Schedule

class ScheduleCreationForm(forms.ModelForm):
    class Meta:
        models = Schedule
        fields = ('name', 'date','time', 'schedule_type','priority')