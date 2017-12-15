from django.test import TestCase
from accounts.forms import SignupForm

class SignupFormTest(TestCase):
    def test_form_has_field(self):
        form = SignupForm()
        expected = ['username','email','password1','password2']
        actual = list(form.fields)
        self.assertSequenceEqual(expected,actual)
