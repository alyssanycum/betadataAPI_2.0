# Generated by Django 3.0.8 on 2020-07-09 16:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.expressions


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Gym',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': (django.db.models.expressions.OrderBy(django.db.models.expressions.F('self.name'), nulls_last=True),),
            },
        ),
        migrations.CreateModel(
            name='Goal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goal_content', models.CharField(max_length=500)),
                ('complete_by', models.DateField()),
                ('is_complete', models.BooleanField()),
                ('completed_on', models.DateField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': (django.db.models.expressions.OrderBy(django.db.models.expressions.F('self.complete_by'), descending=True, nulls_last=True),),
            },
        ),
        migrations.CreateModel(
            name='Climb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('climb_type', models.CharField(max_length=20)),
                ('grade', models.IntegerField()),
                ('description', models.CharField(max_length=300)),
                ('beta_comments', models.CharField(max_length=500)),
                ('rating', models.IntegerField()),
                ('created_on', models.DateTimeField()),
                ('is_archived', models.BooleanField()),
                ('gym', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='betadataApp.Gym')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': (django.db.models.expressions.OrderBy(django.db.models.expressions.F('self.created_on'), descending=True, nulls_last=True),),
            },
        ),
        migrations.CreateModel(
            name='Attempt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attempt_date', models.DateField()),
                ('number_of_falls', models.IntegerField()),
                ('number_of_attempts', models.IntegerField()),
                ('is_flashed', models.BooleanField()),
                ('is_clean', models.BooleanField()),
                ('created_on', models.DateTimeField()),
                ('climb', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='betadataApp.Climb')),
            ],
            options={
                'ordering': (django.db.models.expressions.OrderBy(django.db.models.expressions.F('self.created_on'), descending=True, nulls_last=True),),
            },
        ),
    ]
