# Generated by Django 2.2.6 on 2020-03-07 11:39

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
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=20)),
                ('lastname', models.CharField(max_length=20)),
                ('address', models.CharField(default='', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='TribalYouth',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default='', max_length=50)),
                ('firstname', models.CharField(default='', max_length=50)),
                ('lastname', models.CharField(default='', max_length=50)),
                ('age', models.IntegerField(default=0)),
                ('email', models.EmailField(default='', max_length=50)),
                ('mobile', models.CharField(default='', max_length=10)),
                ('state', models.CharField(default='', max_length=50)),
                ('city', models.CharField(default='', max_length=50)),
                ('address', models.TextField()),
                ('category', models.CharField(default='', max_length=20)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_username', models.CharField(default='', max_length=50)),
                ('company_type', models.CharField(default='', max_length=20)),
                ('company_email', models.EmailField(default='', max_length=50)),
                ('category', models.CharField(default='company-user', max_length=20)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
