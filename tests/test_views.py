from django.core.urlresolvers import reverse
from django.test import TestCase


class SignupViewTestCase(TestCase):

    def test_get(self):
        response = self.client.get(reverse("account_signup"))
        self.assertEqual(response.status_code, 200)

    def test_post(self):
        data = {
            "username": "foo",
            "password": "bar",
            "password_confirm": "bar",
            "email": "foobar@example.com",
        }
        response = self.client.post(reverse("account_signup"), data)
        self.assertEqual(response.status_code, 302)

    def test_closed(self):
        with self.settings(ACCOUNT_OPEN_SIGNUP=False):
            data = {
                "username": "foo",
                "password": "bar",
                "password_confirm": "bar",
                "email": "foobar@example.com",
            }
            response = self.client.post(reverse("account_signup"), data)
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.template_name, "account/signup_closed.html")


class LoginViewTestCase(TestCase):

    def test_get(self):
        response = self.client.get(reverse("account_login"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.template_name, ["account/login.html"])
