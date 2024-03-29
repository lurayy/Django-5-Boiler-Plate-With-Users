from django.forms import ValidationError
from rest_framework import serializers
from django.utils.timezone import now

from subscriptions.apis.serializers.discounts import DiscountRedeemSerializer
from subscriptions.models import FonePayPayment, Payment
from subscriptions.models.discounts import Code, DiscountRedeem
from subscriptions.models.invoice import Invoice
from core.utils.functions import get_properties
from subscriptions.models.subscription import Subscription
from users.api.serializers.userbase import MiniUserBaseSerializer
from users.models.settings import GeneralSettings

from django.db import transaction


class SubscriptionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subscription
        fields = '__all__'


class SubscribeSerializer(serializers.Serializer):
    discount_code = serializers.CharField(required=False)
    subscription_type = serializers.CharField(required=True)

    def validate(self, attrs):
        charge_periods = {'month': 30, 'trimonthly': 90}
        if code := attrs.get('discount_code', None):
            if code := Code.objects.filter(code=code).first():
                if code.is_used:
                    raise ValidationError(
                        'Given discount code is already used.')
                attrs['code'] = code
            else:
                raise ValidationError('Given discount code is Invalid.')
        subscription_type = attrs.get('subscription_type')
        if subscription_type not in charge_periods.keys():
            raise ValidationError(
                'Subscription type must be either "month" or "trimonthly".')
        settings = GeneralSettings.load()
        attrs['subscription_charge'] = getattr(
            settings, f'price_for_{subscription_type}')
        attrs['charged_period'] = charge_periods[subscription_type]
        return super().validate(attrs)

    def create(self, validated_data):
        with transaction.atomic():
            validated_data['created_by'] = self.context['request'].user
            sub = Subscription.objects.create(
                user=self.context['request'].user,
                status='unpaid',
                start_date=int(now().timestamp()))
            invoice = Invoice.objects.create(
                invoiced_by=self.context['request'].user,
                subscription=sub,
                charged_period=validated_data['charged_period'],
                subscription_charge=validated_data['subscription_charge'],
            )
            if code := validated_data.get('code', None):
                DiscountRedeem.objects.create(
                    redeemed_by=self.context['request'].user,
                    code=code,
                    invoice=invoice)
        return invoice


class MiniInvoiceSerializer(serializers.ModelSerializer):
    invoiced_by_details = MiniUserBaseSerializer(source='invoiced_by',
                                                 read_only=True)
    properties = serializers.SerializerMethodField(read_only=True)

    def get_properties(self, obj):
        return get_properties(Invoice, obj)

    class Meta:
        model = Invoice
        exclude = ('id', )


class InvoiceSerializer(MiniInvoiceSerializer):
    subscription_serializer = SubscriptionSerializer(source='subscription',
                                                     read_only=True)
    invoiced_by_details = MiniUserBaseSerializer(source='invoiced_by',
                                                 read_only=True)
    payments = serializers.SerializerMethodField(read_only=True)
    discount_code_used = DiscountRedeemSerializer(source='redeemed_discount',
                                                  read_only=True)

    def get_created_at(self, obj):
        return f"{obj.created_at}"

    def get_payments(self, obj):
        return ''

    class Meta:
        model = Invoice
        exclude = ('id', )


class PaymentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Payment
        fields = '__all__'


class FonePayPaymentSerializer(serializers.ModelSerializer):

    class Meta:
        model = FonePayPayment
        fields = '__all__'


class StaffPaymentSerializer(serializers.Serializer):
    amount = serializers.IntegerField(required=True)

    def validate(self, attrs):
        print('triggered', attrs)
        user = self.context['request'].user
        invoice = self.context['invoice']

        if not user.is_staff:
            raise ValidationError('Unauthorized access.')
        if invoice.is_paid:
            raise ValidationError('Invoice has already been paid.')
        if attrs['amount'] > invoice.bill_amount:
            raise ValidationError('Amount is more than bill amount.')
        return super().validate(attrs)

    def create(self, validated_data):
        with transaction.atomic():
            payment = Payment.objects.create(
                created_by=self.context['request'].user,
                payment_type='staff_approved',
                amount=validated_data['amount'],
                invoice=self.context['invoice'],
                remarks='Staff approved Payment')
            payment.invoice.save()
        return payment.invoice
