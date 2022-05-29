import datetime
from django import forms


class DateInput(forms.DateInput):
    input_type = 'date'


class UserDateForm(forms.Form):
    date = forms.DateField(label='date',
                           initial=datetime.date.today,
                           widget=DateInput,
                           required=True)
