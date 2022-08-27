# Generated by Django 4.1 on 2022-08-27 21:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserTestView',
            fields=[
                ('user_id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=10)),
                ('comp_lessons', models.BigIntegerField()),
                ('daily_goal_id', models.BigIntegerField()),
                ('comp_dg', models.CharField(max_length=25)),
                ('date', models.DateField()),
            ],
            options={
                'db_table': 'learnFrenchApp_usertest_view',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Goal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goal', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=100)),
                ('solution', models.CharField(default='', max_length=100)),
                ('answers', models.ManyToManyField(related_name='answers', to='learnFrench.answer')),
            ],
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('questions', models.ManyToManyField(related_name='questions', to='learnFrench.question')),
            ],
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('title', models.CharField(max_length=70)),
                ('content', models.TextField()),
                ('test', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='learnFrench.test')),
            ],
        ),
        migrations.CreateModel(
            name='UserTest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('completed', models.FloatField()),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('user_test', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='learnFrench.test')),
            ],
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('lessons', models.ManyToManyField(related_name='lessons', to='learnFrench.lesson')),
            ],
        ),
        migrations.CreateModel(
            name='DailyGoal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('daily_goal', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='learnFrench.goal')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'date')},
            },
        ),
    ]