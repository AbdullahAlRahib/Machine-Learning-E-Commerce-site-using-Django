# Generated by Django 3.1.6 on 2022-12-12 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_auto_20221212_1646'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderplaced',
            name='ordered_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
