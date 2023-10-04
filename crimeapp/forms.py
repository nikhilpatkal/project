from django import forms

from crimeapp.models import station_register


class UserForm(forms.ModelForm):
    class Meta():
        model = station_register
        fields = '__all__'