# Generated by Django 3.1.7 on 2021-10-21 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20211021_1855'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='date',
            field=models.DateField(help_text=None),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='phone_number',
            field=models.CharField(blank=True, help_text=None, max_length=14, null=True),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='user_name',
            field=models.CharField(help_text=None, max_length=120),
        ),
    ]
