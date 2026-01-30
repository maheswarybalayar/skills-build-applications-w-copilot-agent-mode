from django.core.management.base import BaseCommand
from octofit_tracker.models import Team, User, Activity, Workout, Leaderboard
from datetime import date

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()
        Workout.objects.all().delete()

        # Create Teams
        marvel = Team.objects.create(name='Marvel', description='Team Marvel Superheroes')
        dc = Team.objects.create(name='DC', description='Team DC Superheroes')

        # Create Users
        users = [
            User(name='Spider-Man', email='spiderman@marvel.com', team=marvel, is_superhero=True),
            User(name='Iron Man', email='ironman@marvel.com', team=marvel, is_superhero=True),
            User(name='Wonder Woman', email='wonderwoman@dc.com', team=dc, is_superhero=True),
            User(name='Batman', email='batman@dc.com', team=dc, is_superhero=True),
        ]
        User.objects.bulk_create(users)

        # Create Workouts
        workouts = [
            Workout(name='Super Strength', description='Strength training for heroes', suggested_for='Marvel'),
            Workout(name='Stealth Training', description='Stealth and agility drills', suggested_for='DC'),
        ]
        Workout.objects.bulk_create(workouts)

        # Create Activities
        spiderman = User.objects.get(email='spiderman@marvel.com')
        batman = User.objects.get(email='batman@dc.com')
        Activity.objects.create(user=spiderman, type='Web Swinging', duration=30, date=date.today())
        Activity.objects.create(user=batman, type='Martial Arts', duration=45, date=date.today())

        # Create Leaderboard
        Leaderboard.objects.create(team=marvel, points=100)
        Leaderboard.objects.create(team=dc, points=90)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data!'))
