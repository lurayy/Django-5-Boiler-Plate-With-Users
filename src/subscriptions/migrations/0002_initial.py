# Generated by Django 5.0 on 2024-02-06 00:26

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('subscriptions', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='discount',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='discounts_created', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='discount',
            name='last_updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='discounts_updated', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='discount',
            name='referred_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='referral_code', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='code',
            name='discount',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='codes', to='subscriptions.discount'),
        ),
        migrations.AddField(
            model_name='discountredeem',
            name='code',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='subscriptions.code'),
        ),
        migrations.AddField(
            model_name='discountredeem',
            name='redeemed_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='invoice',
            name='invoiced_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='invoices', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='discountredeem',
            name='invoice',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='redeemed_discount', to='subscriptions.invoice'),
        ),
        migrations.AddField(
            model_name='payment',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='payments', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='payment',
            name='fonepay_payment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='subscriptions.fonepaypayment'),
        ),
        migrations.AddField(
            model_name='payment',
            name='invoice_summary',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='payments', to='subscriptions.invoice'),
        ),
        migrations.AddField(
            model_name='subscription',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='subscription', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='invoice',
            name='subscription',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='invoice', to='subscriptions.subscription'),
        ),
    ]
