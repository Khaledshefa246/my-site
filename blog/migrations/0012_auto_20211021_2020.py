# Generated by Django 3.1.7 on 2021-10-21 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20211021_2019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='text',
            field=models.TextField(help_text=None, max_length=400),
        ),
        migrations.AlterField(
            model_name='comment',
            name='user_email',
            field=models.EmailField(help_text=None, max_length=254),
        ),
        migrations.AlterField(
            model_name='comment',
            name='user_name',
            field=models.CharField(help_text=None, max_length=120),
        ),
    ]
