# Generated by Django 2.2.5 on 2020-03-30 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20200330_1621'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
