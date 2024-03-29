from django.contrib import admin
from unfold.admin import ModelAdmin
from subscriptions.models.discounts import Code, Discount, DiscountRedeem

from subscriptions.models.invoice import Invoice, Subscription
from subscriptions.models.payments import FonePayPayment, Payment


@admin.register(Invoice)
class InvoiceAdmin(ModelAdmin):
    list_display = ('invoice_number', 'bill_amount', 'paid_amount',
                    'subscription_charge')
    search_fields = ['invoice_number', 'user__username', 'customer_email']
    list_filter = ['is_paid', 'created_at']
    readonly_fields = ('is_paid', )
    autocomplete_fields = [
        'subscription',
    ]


@admin.register(Subscription)
class SubscriptionAdmin(ModelAdmin):
    list_display = (
        'subscription_id',
        'user',
        'status',
        'current_starts',
        'current_period_end',
        'start_date',
    )
    search_fields = ['subscription_id', 'user__username']
    list_filter = [
        'status',
    ]
    readonly_fields = ('status', )
    autocomplete_fields = [
        'user',
    ]


@admin.register(Discount)
class DiscountAdmin(ModelAdmin):
    list_display = (
        'code_prefix',
        'discount_type',
        'value',
        'count_used',
        'count_limit',
        'has_unique_codes',
    )
    search_fields = ('code_prefix', )
    list_filter = ('discount_type', 'has_unique_codes', 'is_limited')
    readonly_fields = ('count_used', )
    autocomplete_fields = ['created_by', 'last_updated_by', 'referred_by']


@admin.register(Code)
class CodeAdmin(ModelAdmin):
    list_display = ('discount', 'code', 'is_used')
    search_fields = ('code', )
    list_filter = ('is_used', )
    readonly_fields = ('code', 'discount')

    def has_add_permission(self, request):
        return False


@admin.register(DiscountRedeem)
class DiscountRedeemAdmin(ModelAdmin):
    list_display = ('redeemed_by', 'code', 'discounted_amount', 'invoice')
    search_fields = ('redeemed_by__email', 'discount__name', 'code__code')
    autocomplete_fields = ['redeemed_by', 'code', 'invoice']

    def code(self, obj):
        return obj.code.code


class FonePayPaymentAdmin(ModelAdmin):
    list_display = ('invoice_number', 'amount', 'qr_status',
                    'is_verified_from_server', 'trace_id', 'ird_details_sent')
    list_filter = ('qr_status', 'is_verified_from_server', 'ird_details_sent')
    search_fields = ('invoice_number', 'amount', 'qr_status')
    readonly_fields = ('last_response_from_fonepay', )


admin.site.register(FonePayPayment, FonePayPaymentAdmin)


class PaymentAdmin(ModelAdmin):
    list_display = ('payment_type', 'amount', 'invoice', 'is_refunded')
    list_filter = ('payment_type', 'is_refunded')
    search_fields = ('payment_type', 'amount', 'invoice__invoice_number')
    autocomplete_fields = ['created_by', 'fonepay_payment', 'invoice']


admin.site.register(Payment, PaymentAdmin)
