# Generated by Django 3.2.8 on 2022-02-26 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20220221_0909'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foods',
            name='Size',
            field=models.CharField(choices=[('Katta', 'Big'), ("O'rtacha", 'Middle'), ('Kichik', 'Little'), ('Maxsus', 'Special')], default='', max_length=15),
        ),
    ]
