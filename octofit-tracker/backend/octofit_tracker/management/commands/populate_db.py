from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Teams
        marvel = Team.objects.create(name='marvel', description='Marvel Team')
        dc = Team.objects.create(name='dc', description='DC Team')

        # Users
        tony = User.objects.create(name='Tony Stark', email='tony@marvel.com', team='marvel')
        steve = User.objects.create(name='Steve Rogers', email='steve@marvel.com', team='marvel')
        bruce = User.objects.create(name='Bruce Wayne', email='bruce@dc.com', team='dc')
        clark = User.objects.create(name='Clark Kent', email='clark@dc.com', team='dc')

        # Activities
        Activity.objects.create(user=tony.name, activity_type='run', duration=30, date='2023-01-01')
        Activity.objects.create(user=steve.name, activity_type='cycle', duration=45, date='2023-01-02')
        Activity.objects.create(user=bruce.name, activity_type='swim', duration=60, date='2023-01-03')
        Activity.objects.create(user=clark.name, activity_type='fly', duration=120, date='2023-01-04')

        # Leaderboard
        Leaderboard.objects.create(user=tony.name, points=100)
        Leaderboard.objects.create(user=steve.name, points=90)
        Leaderboard.objects.create(user=bruce.name, points=110)
        Leaderboard.objects.create(user=clark.name, points=120)

        # Workouts
        Workout.objects.create(name='Pushup', description='Upper body', difficulty='easy')
        Workout.objects.create(name='Squat', description='Lower body', difficulty='medium')
        Workout.objects.create(name='Plank', description='Core', difficulty='hard')

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data!'))
