from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['book_date', 'book_days', 'book_hours', 'status', 'customer', 'user', 'service']

from .models import City  # Ensure this matches your actual model name

class CityForm(forms.ModelForm):
    class Meta:
        model = City
        fields = ['city']  # Add other fields if necessary