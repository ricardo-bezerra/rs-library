# Generated by Django 5.1.3 on 2024-11-25 20:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Condition',
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
        migrations.DeleteModel(
            name='Department',
        ),
        migrations.DeleteModel(
            name='Employee',
        ),
        migrations.DeleteModel(
            name='Function',
        ),
        migrations.DeleteModel(
            name='MaritalStatus',
        ),
        migrations.DeleteModel(
            name='PaymentMethod',
        ),
        migrations.DeleteModel(
            name='Rent',
        ),
        migrations.DeleteModel(
            name='Sale',
        ),
    ]