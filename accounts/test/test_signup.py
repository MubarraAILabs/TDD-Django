from django.test import TestCase
from django.urls import reverse
from http import HTTPStatus
from django.contrib.auth.forms import UserCreationForm
from accounts.forms import UserRegistrationForm
from django.contrib.auth import get_user_model

# Create your tests here.

User = get_user_model()

class AccountCreationTest(TestCase):
    
    def setUp(self) -> None:
        self.form_class = UserRegistrationForm
    
    def test_signup_page_exists(self):
        response = self.client.get(reverse('signup_page'))
        
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, 'accounts/register.html')
        self.assertContains(response, "Cretae your account today!")
        
    def test_signup_page_works_correctly(self):
        
        
        self.assertTrue(issubclass(self.form_class, UserCreationForm))
        self.assertTrue('email' in self.form_class.Meta.fields)
        self.assertTrue('username' in self.form_class.Meta.fields)
        self.assertTrue('password1' in self.form_class.Meta.fields)
        self.assertTrue('password2' in self.form_class.Meta.fields)
        
        sample_data = {
            'username': 'testuser',
            'email': 'mahi@gmail.com',
            'password1': 'Complexpassword123',
            'password2': 'Complexpassword123'
        }
        
        form = self.form_class(sample_data)
        self.assertTrue(form.is_valid())
        
    def test_signup_form_creates_user_in_db(self):
         user = {
            'username': 'testuser1',
            'email': 'mahi1@gmail.com',
            'password1': 'Complexpassword123',
            'password2': 'Complexpassword123'
        }
         
         form = self.form_class(user)
         if form.is_valid():
             form.save()
        
         self.assertEqual(User.objects.count(), 1)
        
        
