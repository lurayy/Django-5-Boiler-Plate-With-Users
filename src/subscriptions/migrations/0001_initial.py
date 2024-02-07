# Generated by Django 5.0 on 2024-02-08 02:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Code',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('code', models.CharField(max_length=255, unique=True)),
                ('is_used', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['-is_active', '-id'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('description', models.TextField(default='')),
                ('code_prefix', models.CharField(max_length=255, unique=True)),
                ('discount_type', models.CharField(choices=[('percent', 'Percent'), ('fixed', 'Fixed')], default='fixed', max_length=8)),
                ('value', models.DecimalField(decimal_places=2, default=0.0, max_digits=60)),
                ('is_limited', models.BooleanField(default=False)),
                ('count_used', models.PositiveIntegerField(default=0)),
                ('count_limit', models.PositiveIntegerField(default=1)),
                ('has_unique_codes', models.BooleanField(default=False)),
                ('is_available', models.BooleanField(default=False)),
                ('is_referral', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ['-is_active', '-id'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DiscountRedeem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('discounted_amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=60)),
            ],
            options={
                'ordering': ['-is_active', '-id'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FonePayPayment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('qr_status', models.CharField(choices=[('initiated', 'initiated'), ('requested', 'requested'), ('failed', 'failed'), ('success', 'success')], default='initiated', max_length=255)),
                ('amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=60)),
                ('last_response_from_fonepay', models.TextField(blank=True, null=True)),
                ('invoice_number', models.CharField(max_length=255)),
                ('is_verified_from_server', models.BooleanField(default=False)),
                ('trace_id', models.TextField(blank=True, default='', null=True)),
                ('ird_details_sent', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['-is_active', '-id'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('invoice_number', models.CharField(blank=True, default='', max_length=50, null=True, unique=True)),
                ('subscription_charge', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('charged_period', models.PositiveIntegerField(default=30)),
                ('staff_discount_amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('staff_discount_remarks', models.CharField(blank=True, default='', max_length=255)),
                ('total_discount_amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('bill_amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('paid_amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('is_paid', models.BooleanField(default=False)),
                ('is_charged_period_added', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['-is_active', '-id'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('payment_type', models.CharField(choices=[('fonepay', 'Fonepay'), ('staff_approved', 'Staff Approved'), ('stripe', 'Stripe')], default='fonepay', max_length=15)),
                ('amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=60)),
                ('remarks', models.TextField(blank=True, default='')),
                ('is_refunded', models.BooleanField(default=False)),
                ('refunded_remarks', models.TextField(blank=True, default='')),
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
