# Generated by Django 4.1.7 on 2023-05-03 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crimeapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserCharCertificateData1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('char_date', models.DateField()),
                ('char_fullname', models.CharField(max_length=200)),
                ('char_adhar', models.CharField(max_length=15)),
                ('char_age', models.IntegerField()),
                ('char_gender', models.CharField(max_length=200)),
                ('char_phone', models.CharField(max_length=20)),
                ('char_police_station', models.CharField(max_length=200)),
                ('char_address', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='UserFeedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fed_date', models.DateField()),
                ('fed_name', models.CharField(max_length=100)),
                ('fed_email', models.CharField(max_length=100)),
                ('fed_subject', models.CharField(max_length=200)),
                ('fed_message', models.TextField()),
                ('fed_stationname', models.CharField(max_length=100)),
            ],
        ),
    ]
