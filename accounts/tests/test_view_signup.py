from django.test import TestCase
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.urls import resolve
from accounts.views import signup
from django.contrib.auth.forms import UserCreationForm
from accounts.forms import SignupForm



class SignupTests(TestCase):
    def setUp(self):
        url = reverse('signup')
        self.response = self.client.get(url)

    def test_signup_status_code(self):
        self.assertEquals(self.response.status_code, 200)

    def test_url_resolver_signup_view(self):
        view = resolve('/signup/')
        self.assertEquals(view.func,signup)

    def test_csrf(self):
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_contains_form(self):
        form = self.response.context.get('form')
        self.assertIsInstance(form, SignupForm)

    def test_form_inputs(self):
        self.assertContains(self.response, '<input', 5)
        self.assertContains(self.response, 'type="text"', 1)
        self.assertContains(self.response, 'type="email"',1)
        self.assertContains(self.response,'type="password"',2)

class SuccessfulSignupTests(TestCase):

    def setUp(self):
        url = reverse('signup')
        data = {'username':'lina', 'password1':'zaid4timesaday','password2':'zaid4timesaday', 'email':'albardn2@illinois.edu'}
        self.response = self.client.post(url,data)
        self.home_url = reverse('home')


    def test_redirection(self):
        self.assertRedirects(self.response, self.home_url)

    def test_user_creation(self):
        self.assertTrue(User.objects.exists())

    def test_user_authentication(self):
        response = self.client.get(self.home_url)
        user = response.context.get('user')
        self.assertTrue(user.is_authenticated)



class invalidSignupTests(TestCase):

    def setUp(self):
        url = reverse('signup')
        data = {'username':'iman', 'password1':'123', 'password2':'123'}


        self.response = self.client.post(url,data)
        self.home_url = reverse('home')

    def test_signup_status_code(self):
        self.assertEquals(self.response.status_code, 200)

    def test_form_errors(self):
        form = self.response.context.get('form')
        self.assertTrue(form.errors)

    def test_dont_create_user(self):
        self.assertFalse(User.objects.exists())
