# Generated by Django 3.2.13 on 2022-12-09 01:57

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Mylotations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Park',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manageNo', models.CharField(max_length=200)),
                ('parkName', models.CharField(max_length=300)),
                ('parkType', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=500)),
                ('latitude', models.CharField(max_length=200)),
                ('longitude', models.CharField(max_length=200)),
                ('size', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Dogroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(default=datetime.datetime.now)),
                ('title', models.CharField(max_length=20)),
                ('membercnt', models.IntegerField(default=5)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('dog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.dog')),
                ('join', models.ManyToManyField(related_name='joiner', to=settings.AUTH_USER_MODEL)),
                ('park', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='walkings.park')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
