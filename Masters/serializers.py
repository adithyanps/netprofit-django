from rest_framework import serializers,fields
from Masters.models import (
        Partner,
        Branch,
        Area,
        Product,
        ProductCategory,
        # JournalEntry,
        Account,
        AccountDefault,
        # JournalItem,
        # ChildInvoice,Parent,
        # InvoiceLineOld,
        # InvoiceLine,
        # SalesInvoice,
        # SalesInvoiceNu,
        # CustomerReceipt,
        # ExpenseCategory,
        # Expenses,
        # YearCharts,
        # ExpenseYearChart,
        # CreditNote,
        # CreditNoteNumber
        )
from rest_framework.validators import UniqueTogetherValidator
from drf_writable_nested import WritableNestedModelSerializer


class PartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partner
        fields = "__all__"

class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = ['id','branch']

class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area
        fields = "__all__"

class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = "__all__"


class ItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id','item','price','product_Cat']

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = "__all__"

class AccountDefaultSerializer(serializers.ModelSerializer):

    class Meta:
        model = AccountDefault
        fields = "__all__"

    def to_representation(self, instance):
        response = super().to_representation(instance)

        response['SalesAccont'] = AccountSerializer(instance.SalesAccont).data
        response['PurchaseAccont'] = AccountSerializer(instance.PurchaseAccont).data
        response['CustomerAccount'] = AccountSerializer(instance.CustomerAccount).data
        response['SupplierAccount'] = AccountSerializer(instance.SupplierAccount).data

        return response
