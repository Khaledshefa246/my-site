# Generated by Django 3.1.7 on 2021-10-09 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20210918_2026'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='pdf_word_file',
            field=models.FileField(max_length=150, null=True, upload_to='pdf word'),
        ),
    ]
