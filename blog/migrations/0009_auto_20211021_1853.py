# Generated by Django 3.1.7 on 2021-10-21 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_post_pdf_word_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='branch',
            field=models.CharField(choices=[('Heliopolis', 'Heliopolis'), ('Maadi', 'Maadi')], default='Maadi', max_length=120),
        ),
    ]