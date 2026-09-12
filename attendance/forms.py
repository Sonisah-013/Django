from django import forms
from .models import AttendanceRecord

class DailyAttendanceForm(forms.Form):
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))