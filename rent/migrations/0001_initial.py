# Generated by Django 5.1.3 on 2024-11-25 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rent',
            fields=[
                ('rent_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('rent_date', models.DateField(blank=True, default='')),
                ('rent_invoice', models.CharField(max_length=25)),
                ('rent_product', models.CharField(max_length=55)),
                ('rent_amount_product', models.FloatField()),
                ('rent_payment_method', models.IntegerField()),
                ('rent_condition', models.IntegerField()),
                ('rent_descount', models.FloatField()),
                ('rent_taxes', models.FloatField()),
                ('rent_employee_commission', models.FloatField(blank=True, default='')),
                ('rent_start_date', models.DateField(blank=True, default='')),
                ('rent_end_date', models.DateField(blank=True, default='')),
                ('book_id', models.IntegerField()),
                ('employee_id', models.IntegerField()),
                ('customer_id', models.IntegerField()),
                ('condition_id', models.IntegerField()),
                ('payment_method_id', models.IntegerField()),
            ],
        ),
    ]
