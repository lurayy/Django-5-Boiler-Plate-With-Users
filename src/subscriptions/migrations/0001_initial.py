# Generated by Django 5.0 on 2024-02-03 12:49

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('invoice_number', models.CharField(default='', max_length=50, unique=True)),
                ('invoiced_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('paid_for_in_days', models.PositiveIntegerField(default=30)),
                ('amount_paid', models.PositiveIntegerField(default=0)),
                ('amount_due', models.PositiveIntegerField(default=0)),
                ('customer_email', models.CharField(default='', max_length=255)),
                ('status', models.CharField(default='draft', max_length=255)),
            ],
            options={
                'ordering': ['-is_active', '-id'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subscription_id', models.CharField(blank=True, default='', max_length=255, unique=True)),
                ('status', models.CharField(default='deactivated', max_length=255)),
                ('current_starts', models.PositiveBigIntegerField(default=0)),
                ('current_period_end', models.PositiveBigIntegerField(default=0)),
                ('start_date', models.PositiveBigIntegerField(default=0)),
            ],
        ),
    ]
