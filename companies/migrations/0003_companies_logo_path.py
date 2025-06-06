# Generated by Django 4.1.7 on 2025-05-20 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0002_remove_companies_grade_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='companies',
            name='logo_path',
            field=models.CharField(blank=True, help_text="Path to logo image in static/, e.g., 'images/logos/company1.png'", max_length=255),
        ),
    ]
