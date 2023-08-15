# Generated by Django 4.2 on 2023-04-27 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('covid', '0003_alter_country_aged_65_older_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='aged_65_older',
            field=models.DecimalField(decimal_places=3, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='country',
            name='aged_70_older',
            field=models.DecimalField(decimal_places=3, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='country',
            name='cardiovasc_death_rate',
            field=models.DecimalField(decimal_places=3, max_digits=6, null=True),
        ),
        migrations.AlterField(
            model_name='country',
            name='diabetes_prevalence',
            field=models.DecimalField(decimal_places=2, max_digits=4, null=True),
        ),
        migrations.AlterField(
            model_name='country',
            name='extreme_poverty',
            field=models.DecimalField(decimal_places=1, max_digits=3, null=True),
        ),
        migrations.AlterField(
            model_name='country',
            name='female_smokers',
            field=models.DecimalField(decimal_places=1, max_digits=3, null=True),
        ),
        migrations.AlterField(
            model_name='country',
            name='gdp_per_capita',
            field=models.DecimalField(decimal_places=3, max_digits=9, null=True),
        ),
        migrations.AlterField(
            model_name='country',
            name='handwashing_facilities',
            field=models.DecimalField(decimal_places=3, max_digits=6, null=True),
        ),
        migrations.AlterField(
            model_name='country',
            name='hospital_beds_per_thousand',
            field=models.DecimalField(decimal_places=3, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='country',
            name='life_expectancy',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='country',
            name='male_smokers',
            field=models.DecimalField(decimal_places=1, max_digits=3, null=True),
        ),
        migrations.AlterField(
            model_name='country',
            name='median_age',
            field=models.DecimalField(decimal_places=1, max_digits=3, null=True),
        ),
        migrations.AlterField(
            model_name='country',
            name='population',
            field=models.DecimalField(decimal_places=1, max_digits=11, null=True),
        ),
        migrations.AlterField(
            model_name='country',
            name='population_density',
            field=models.DecimalField(decimal_places=3, max_digits=8, null=True),
        ),
        migrations.AlterField(
            model_name='country',
            name='stringency_index',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
    ]
