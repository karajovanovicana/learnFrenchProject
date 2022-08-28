from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Answer(models.Model):
    answer = models.CharField(max_length=100)

    def __str__(self):
        return self.answer


class Question(models.Model):
    question = models.CharField(max_length=100)
    answers = models.ManyToManyField(Answer, 'answers')
    solution = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.question


class Test(models.Model):
    title = models.CharField(max_length=100)
    questions = models.ManyToManyField(Question, related_name='questions')

    def __str__(self):
        return self.title


class Lesson(models.Model):
    title = models.CharField(max_length=70)
    content = models.TextField()
    test = models.OneToOneField(Test, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.title


class Unit(models.Model):
    title = models.CharField(max_length=100)
    lessons = models.ManyToManyField(Lesson, related_name='lessons')

    def __str__(self):
        return self.title


class Goal(models.Model):
    goal = models.CharField(max_length=20)

    def __str__(self):
        return self.goal


class DailyGoal(models.Model):
    daily_goal = models.ForeignKey(Goal, on_delete=models.CASCADE, null=True, blank=True)
    # lessons = models.ManyToManyField(Lesson, related_name='lessons_profile')
    date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        unique_together = ("user", "date")


class UserTest(models.Model):
    user_test = models.ForeignKey(Test, on_delete=models.CASCADE, null=True, blank=True)
    date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    completed = models.FloatField()

    # class Meta:
    #     unique_together = ("user", "date", "completed", "user_test")


class UserTestView(models.Model):
    user_id = models.BigIntegerField(primary_key=True)
    username=models.CharField(max_length=10)
    comp_lessons = models.BigIntegerField()
    daily_goal_id = models.BigIntegerField()
    comp_dg = models.CharField(max_length=25)
    date = models.DateField()

    class Meta:
        managed = False
        db_table = 'learnfrenchapp_usertest_view'

