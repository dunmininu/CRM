from django.test import TestCase
from django.urls import reverse

# Create your tests here.

class LandingPageTest(TestCase):

    def test_get(self):
        response = self.client.get(reverse('landing_page'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "landing.html")

class LoginViewTest(TestCase):
    def test_login(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "registration/login.html")
        