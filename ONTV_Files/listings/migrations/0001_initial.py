# Generated by Django 2.2.6 on 2019-11-23 13:55

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('developers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('marketbias', models.CharField(choices=[('BEAR', 'Bearish'), ('BULL', 'Bullish'), ('NEUTRAL', 'Neutral')], default='NEUTRAL', max_length=8)),
                ('description', models.TextField(blank=True)),
                ('promotion', models.CharField(max_length=10)),
                ('price', models.IntegerField()),
                ('maxloss', models.DecimalField(decimal_places=2, max_digits=4)),
                ('maxprofit', models.DecimalField(decimal_places=2, max_digits=4)),
                ('photo_main', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('photo_1', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('photo_2', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('photo_3', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('photo_4', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('photo_5', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('photo_6', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('is_published', models.BooleanField(default=True)),
                ('list_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('developer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='developers.Developer')),
            ],
        ),
    ]