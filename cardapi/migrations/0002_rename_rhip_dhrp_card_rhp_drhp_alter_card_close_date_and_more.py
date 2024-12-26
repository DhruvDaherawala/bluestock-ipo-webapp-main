# Generated by Django 4.2.15 on 2024-08-22 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cardapi', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='card',
            old_name='rhip_dhrp',
            new_name='rhp_drhp',
        ),
        migrations.AlterField(
            model_name='card',
            name='close_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='card',
            name='listing_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='card',
            name='open_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]