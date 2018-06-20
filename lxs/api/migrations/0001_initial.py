# Generated by Django 2.0.3 on 2018-06-20 04:20

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('role', models.CharField(choices=[('interviewer', 'Interviewer'), ('candidate', 'Candidate')], max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Interview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('slot', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(23)])),
                ('candidate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Actor')),
                ('interviewers', models.ManyToManyField(related_name='appointments', to='api.Actor')),
            ],
        ),
        migrations.CreateModel(
            name='Slot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weekday', models.CharField(choices=[('monday', 'Monday'), ('tuesday', 'Tuesday'), ('wednesday', 'Wednesday'), ('thursday', 'Thursday'), ('friday', 'Friday')], max_length=30)),
                ('start', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(23)])),
                ('actor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Actor')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='interview',
            unique_together={('candidate', 'date', 'slot')},
        ),
    ]
