# Generated by Django 2.0.2 on 2018-02-18 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userdata', '0004_auto_20180218_0934'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applieduser',
            name='citizenship_number',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='applieduser',
            name='country',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='applieduser',
            name='course',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='applieduser',
            name='date_of_birth',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='applieduser',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='applieduser',
            name='first_name',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='applieduser',
            name='intake',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='applieduser',
            name='last_name',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='applieduser',
            name='marital_status',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='applieduser',
            name='mobile',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='applieduser',
            name='nationality',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='applieduser',
            name='permanent_country',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='applieduser',
            name='photograph',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='applieduser',
            name='place_of_birth',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='applieduser',
            name='responsibilites',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='applieduser',
            name='resume',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='applieduser',
            name='sex',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='applieduser',
            name='statement_of_purpose',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='applieduser',
            name='title',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
    ]