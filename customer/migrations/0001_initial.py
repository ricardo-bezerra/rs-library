# Generated by Django 5.1.3 on 2024-11-25 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('customer_id', models.UUIDField(editable=False, primary_key=True, serialize=False)),
                ('customer_name', models.CharField(max_length=25)),
                ('customer_surname', models.CharField(max_length=55)),
                ('customer_location', models.CharField(max_length=25)),
                ('employee_zipcode', models.CharField(max_length=25)),
                ('employee_birth', models.DateField(blank=True, default='')),
                ('customer_address', models.CharField(max_length=150)),
                ('customer_job_type', models.CharField(max_length=35)),
                ('customer_create_at', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
