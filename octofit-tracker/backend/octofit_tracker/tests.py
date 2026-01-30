from django.test import TestCase
from rest_framework.test import APIClient
from .models import Team, User, Activity, Workout, Leaderboard

class APITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.team = Team.objects.create(name='Test Team', description='A test team')
        self.user = User.objects.create(name='Test User', email='test@example.com', team=self.team, is_superhero=True)
        self.workout = Workout.objects.create(name='Test Workout', description='A test workout', suggested_for='Test Team')
        self.activity = Activity.objects.create(user=self.user, type='Test Activity', duration=60, date='2023-01-01')
        self.leaderboard = Leaderboard.objects.create(team=self.team, points=50)

    def test_api_root(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('users', response.data)

    def test_user_list(self):
        response = self.client.get('/api/users/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

    def test_team_list(self):
        response = self.client.get('/api/teams/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

    def test_activity_list(self):
        response = self.client.get('/api/activities/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

    def test_workout_list(self):
        response = self.client.get('/api/workouts/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

    def test_leaderboard_list(self):
        response = self.client.get('/api/leaderboards/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
