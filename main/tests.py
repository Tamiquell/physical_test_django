import datetime

from django.test import TestCase
from .forms import UserDateForm


class FormTests(TestCase):
    def test_forms(self):
        form_data = {'date': datetime.date.today()}
        form = UserDateForm(data=form_data)
        self.assertTrue(form.is_valid())
