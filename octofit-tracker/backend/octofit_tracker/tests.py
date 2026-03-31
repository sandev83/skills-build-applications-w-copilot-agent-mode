from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class UserModelTest(TestCase):
    def test_create_user(self):
        user = User.objects.create(name="Test User", email="test@example.com", team="Test Team")
        self.assertEqual(user.name, "Test User")
        self.assertEqual(user.email, "test@example.com")
        self.assertEqual(user.team, "Test Team")

class TeamModelTest(TestCase):
    def test_create_team(self):
        team = Team.objects.create(name="Test Team", members=["user1", "user2"])
        self.assertEqual(team.name, "Test Team")
        self.assertEqual(team.members, ["user1", "user2"])

class ActivityModelTest(TestCase):
    def test_create_activity(self):
        activity = Activity.objects.create(user="Test User", activity="Running", duration=30)
        self.assertEqual(activity.user, "Test User")
        self.assertEqual(activity.activity, "Running")
        self.assertEqual(activity.duration, 30)

class LeaderboardModelTest(TestCase):
    def test_create_leaderboard(self):
        leaderboard = Leaderboard.objects.create(team="Test Team", points=100)
        self.assertEqual(leaderboard.team, "Test Team")
        self.assertEqual(leaderboard.points, 100)

class WorkoutModelTest(TestCase):
    def test_create_workout(self):
        workout = Workout.objects.create(user="Test User", workout="Pushups", duration=15)
        self.assertEqual(workout.user, "Test User")
        self.assertEqual(workout.workout, "Pushups")
        self.assertEqual(workout.duration, 15)
