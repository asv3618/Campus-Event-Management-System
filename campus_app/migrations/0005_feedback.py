# Generated by Django 4.1.5 on 2024-04-19 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campus_app', '0004_registration'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('feedbackId', models.AutoField(primary_key=True, serialize=False)),
                ('eventId', models.IntegerField()),
                ('userId', models.IntegerField()),
                ('feedbackDate', models.DateField(auto_now_add=True)),
                ('feedback', models.CharField(max_length=300)),
                ('rating', models.IntegerField()),
            ],
        ),
    ]
