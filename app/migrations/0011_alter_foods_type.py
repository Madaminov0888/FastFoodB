# Generated by Django 3.2.8 on 2022-02-28 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_alter_foods_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foods',
            name='type',
            field=models.CharField(choices=[('Lavash', 'Lavash'), ('Chizburger', 'Chizburger'), ('Pizza', 'Pizza'), ('TurkchaPitsa', 'Pide'), ('Hotdog', 'Hotdog'), ('Doner', 'Doner'), ('Ichimliklar', 'Ichimliklar'), ('Kavob', 'Kebab')], max_length=15),
        ),
    ]
