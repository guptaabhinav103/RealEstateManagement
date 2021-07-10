# Generated by Django 3.1.5 on 2021-06-03 19:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=50, unique=True)),
                ('contact', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=50)),
                ('username', models.CharField(max_length=50, unique=True)),
                ('contact', models.IntegerField()),
                ('password', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('desc', models.TextField()),
                ('prop_image', models.FileField(blank=True, null=True, upload_to='media/%Y/%m/%d')),
                ('property_type', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=35)),
                ('location', models.CharField(max_length=200, unique=True)),
                ('Owner', models.ForeignKey(default='ABC', on_delete=django.db.models.deletion.CASCADE, to='Home.owner')),
            ],
        ),
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(unique=True)),
                ('desc', models.TextField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Property_2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agent', models.ForeignKey(default='ABC', on_delete=django.db.models.deletion.CASCADE, to='Home.agent')),
                ('property', models.ForeignKey(default='ABC', on_delete=django.db.models.deletion.CASCADE, to='Home.property')),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=50, unique=True)),
                ('contact', models.IntegerField()),
                ('address', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='media/%Y/%m/%d')),
                ('registration', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Home.registration')),
            ],
        ),
        migrations.CreateModel(
            name='Appointment_2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Home.agent')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Home.owner')),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(null=True, unique=True)),
                ('desc', models.CharField(max_length=500, null=True)),
                ('status', models.CharField(max_length=50, null=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Home.customer')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Home.owner')),
            ],
        ),
    ]
