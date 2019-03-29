from django import forms
from .models import Booking

class CheckinForm(forms.ModelForm):

    class Meta:
        model = Booking
        fields = ['start_date', 'end_date']
