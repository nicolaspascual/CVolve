# Generated by Django 2.2.6 on 2019-10-12 08:39

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobOffer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, verbose_name='Title')),
                ('description', models.TextField(verbose_name='Description')),
                ('responsibilities', models.TextField(verbose_name='Responsibilities')),
                ('minimum_requirements', models.TextField(verbose_name='Minimum Requirements')),
                ('preferred_requirements', models.TextField(blank=True, null=True, verbose_name='Preferred Requirements')),
                ('type', models.CharField(max_length=80, verbose_name='Type')),
                ('compensation', models.FloatField(blank=True, null=True, verbose_name='Compensation')),
                ('duration', models.IntegerField(blank=True, null=True, verbose_name='Duration')),
                ('duration_unit', models.CharField(blank=True, max_length=20, null=True, verbose_name='Duration Unit')),
                ('company', models.CharField(max_length=120, verbose_name='Company')),
                ('department', models.CharField(max_length=120, verbose_name='Department')),
                ('city', models.CharField(max_length=120, verbose_name='City')),
                ('state', models.CharField(max_length=120, verbose_name='State')),
                ('country', models.CharField(max_length=120, verbose_name='Country')),
            ],
            options={
                'verbose_name_plural': 'JobOffers',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('surnames', models.CharField(max_length=150, verbose_name='Surnames')),
                ('mail', models.CharField(max_length=50, verbose_name='Mail')),
                ('phone', models.CharField(max_length=50, verbose_name='Phone')),
                ('summary', models.TextField(verbose_name='Summary')),
                ('skills', models.TextField(verbose_name='Skills')),
                ('languages', models.TextField(verbose_name='Languages')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='UserProjects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='Name')),
                ('summary', models.TextField(verbose_name='Summary')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.User')),
            ],
            options={
                'verbose_name_plural': 'UserProjects',
            },
        ),
        migrations.CreateModel(
            name='UserExperience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(max_length=150, verbose_name='Role')),
                ('company', models.CharField(max_length=150, verbose_name='Company')),
                ('start_date', models.DateField(verbose_name='Start Date')),
                ('end_date', models.DateField(blank=True, null=True, verbose_name='End Date')),
                ('summary', models.TextField(verbose_name='Summary')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.User')),
            ],
            options={
                'verbose_name_plural': 'UserExperiences',
            },
        ),
        migrations.CreateModel(
            name='UserEducation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Title')),
                ('institution', models.CharField(max_length=150, verbose_name='Institution')),
                ('start_date', models.DateField(verbose_name='Start Date')),
                ('end_date', models.DateField(blank=True, null=True, verbose_name='End Date')),
                ('summary', models.TextField(verbose_name='Summary')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.User')),
            ],
            options={
                'verbose_name_plural': 'UserEducations',
            },
        ),
    ]