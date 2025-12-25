from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token
from .models import Experience

class ExperienceAPITest(TestCase):
    def setUp(self):
        self.user = User.objects.create_superuser('admin', 'admin@example.com', 'password123')
        self.token = Token.objects.create(user=self.user)
        self.client = APIClient()
        self.experience_url = '/api/experience/'

    def test_create_experience_authenticated(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        data = {
            "company": "Tech Corp",
            "role": "Senior Dev",
            "start_date": "2023-01-01",
            "description": "Built cool stuff"
        }
        response = self.client.post(self.experience_url, data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Experience.objects.count(), 1)
        self.assertEqual(Experience.objects.get().company, "Tech Corp")

    def test_create_experience_unauthenticated(self):
        self.client.credentials() # No auth
        data = {
            "company": "Tech Corp",
            "role": "Senior Dev",
            "start_date": "2023-01-01",
            "description": "Built cool stuff"
        }
        response = self.client.post(self.experience_url, data)
        self.assertEqual(response.status_code, 401)
        self.assertEqual(Experience.objects.count(), 0)

    def test_list_experience_public(self):
        Experience.objects.create(
            company="Old Job",
            role="Junior Dev",
            start_date="2020-01-01",
            description="Learned stuff"
        )
        response = self.client.get(self.experience_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data['results']), 1)
