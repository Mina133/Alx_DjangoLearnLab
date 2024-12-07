from django.test import TestCase

# Create your tests here.

def test_logout_view_redirects_to_login_page(self):
    response = self.client.get('/logout/')
    self.assertRedirects(response, '/login_page')
