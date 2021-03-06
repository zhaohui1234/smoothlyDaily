# Generated by Django 2.2.3 on 2019-08-01 03:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=30)),
                ('wx_name', models.CharField(max_length=100)),
                ('create_time', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seq', models.CharField(max_length=20)),
                ('create_time', models.DateTimeField(auto_now=True)),
                ('end_time', models.DateTimeField(auto_now=True)),
                ('state', models.CharField(max_length=100)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='run.User')),
            ],
        ),
    ]
