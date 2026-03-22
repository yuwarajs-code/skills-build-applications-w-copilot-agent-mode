from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        self.stdout.write(self.style.WARNING('Deleting old data...'))
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Workout.objects.all().delete()
        Leaderboard.objects.all().delete()

        self.stdout.write(self.style.SUCCESS('Creating teams...'))
        marvel = Team.objects.create(name='marvel', description='Marvel Team')
        dc = Team.objects.create(name='dc', description='DC Team')

        self.stdout.write(self.style.SUCCESS('Creating users...'))
        users = [
            User.objects.create(email='ironman@marvel.com', name='Iron Man', team=marvel.name),
            User.objects.create(email='captain@marvel.com', name='Captain America', team=marvel.name),
            User.objects.create(email='batman@dc.com', name='Batman', team=dc.name),
            User.objects.create(email='superman@dc.com', name='Superman', team=dc.name),
        ]

        self.stdout.write(self.style.SUCCESS('Creating workouts...'))
        workouts = [
            Workout.objects.create(name='Pushups', description='Do pushups', difficulty='easy'),
            Workout.objects.create(name='Running', description='Run 5km', difficulty='medium'),
        ]

        self.stdout.write(self.style.SUCCESS('Creating activities...'))
        Activity.objects.create(user=users[0], type='run', duration=30, date=timezone.now().date())
        Activity.objects.create(user=users[1], type='pushup', duration=15, date=timezone.now().date())
        Activity.objects.create(user=users[2], type='run', duration=25, date=timezone.now().date())
        Activity.objects.create(user=users[3], type='pushup', duration=20, date=timezone.now().date())

        self.stdout.write(self.style.SUCCESS('Creating leaderboard...'))
        Leaderboard.objects.create(user=users[0], score=100, rank=1)
        Leaderboard.objects.create(user=users[1], score=90, rank=2)
        Leaderboard.objects.create(user=users[2], score=80, rank=3)
        Leaderboard.objects.create(user=users[3], score=70, rank=4)

        self.stdout.write(self.style.SUCCESS('Database populated with test data!'))
