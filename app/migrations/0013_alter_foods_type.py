# Generated by Django 3.2.8 on 2022-03-09 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_remove_foods_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foods',
            name='type',
            field=models.CharField(choices=[('Lavash', 'Lavash'), ('Chizburger', 'Chizburger'), ('Pizza', 'Pizza'), ('TurkchaPitsa', 'Pide'), ('Hotdog', 'Hotdog'), ('Doner', 'Doner'), ('Ichimliklar', 'Ichimliklar'), ('Kavob', 'Kebab'), ('Frie', 'Frie')], max_length=15),
        ),
    ]
