# Generated by Django 3.2.8 on 2022-02-28 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_alter_foods_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foods',
            name='type',
            field=models.CharField(choices=[('Lavash', 'Lavash'), ('Chizburger', 'Chizburger'), ('Pizza', 'Pizza'), ('TurkchaPitsa', 'Pide'), ('Hotdog', 'Hotdog'), ('Ichimliklar', 'Ichimliklar'), ('Kavob', 'Kebab')], max_length=15),
        ),
    ]
