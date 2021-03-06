# Generated by Django 3.2.8 on 2022-02-19 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20220218_1024'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='botuser',
            name='user',
        ),
        migrations.AddField(
            model_name='botuser',
            name='chat_id',
            field=models.IntegerField(auto_created=True, blank=True, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='botuser',
            name='full_name',
            field=models.CharField(auto_created=True, blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='foods',
            name='Size',
            field=models.CharField(choices=[('Katta', 'Big'), ("O'rtacha", 'Middle'), ('Oddiy', 'Little'), ('Maxsus', 'Special')], default='', max_length=15),
        ),
        migrations.AlterField(
            model_name='foods',
            name='type',
            field=models.CharField(choices=[('Lavash', 'Lavash'), ('Chizburger', 'Chizburger'), ('Pizza', 'Pizza'), ('Turkcha pitsa', 'Shaverma'), ('Hotdog', 'Hotdog'), ('Ichimliklar', 'Ichimliklar'), ('Kavob', 'Kebab')], max_length=15),
        ),
    ]
