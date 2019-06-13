from rest_framework import serializers,fields
from core.models import (
        Customer,Branch,Item,
        JournalEntry,Account,JournalItem,
        ChildInvoice,Parent,
        SalesInvoice,
        AccountDefault,CustomerReceipt,
        ExpenseCategory,Expenses,
        InvoiceLine
        )
from rest_framework.validators import UniqueTogetherValidator
from drf_writable_nested import WritableNestedModelSerializer

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id','customer']


class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = ['id','branch']


class ItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['id','item','price']

class ChildInvoiceSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = ChildInvoice
        fields = [
            'id',
            'key',
            'item','price','quantity','sub_total'
        ]
        read_only_fields = ('key',)
        # depth = 1

class InvoiceLineSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvoiceLine
        fields = "__all__"


class ParentInvoiceSerializer(serializers.ModelSerializer):
    child = ChildInvoiceSerializer(many=True)

    class Meta:
        model = Parent
        fields = [
            "id",
            'invoice_no', 'doc_no',
            'customer', 'branch', 'status',
            'narration', 'date', 'total_amount',
            'discount', 'grant_total',
            'journal_entry',
            "child",
        ]
        # read_only_fields = ["tags"]
    def create(self, validated_data):
        journal_entry_instance = JournalEntry.objects.create(date=validated_data['date'],
                                                             description=validated_data['narration'])
       # #'transaction_type' will be "SALES" by default
        # account_instance = Account.objects.create(name="some name")
        account_instance = Account.objects.get(pk=1)
       #
        journal_item_instnce = JournalItem.objects.create(journal_entry=journal_entry_instance,
                                                          account=account_instance,
                                                          debit_amount=validated_data['total_amount'],
                                                          credit_amount=validated_data['total_amount'])

        child = validated_data.pop('child',[])
        key = Parent.objects.create(journal_entry=journal_entry_instance, **validated_data)
        # key = Parent.objects.create( **validated_data)

        for choice in child:
            ChildInvoice.objects.create(**choice, key=key)
        return key

    def update(self, instance, validated_data):
        child = validated_data.pop('child')
        instance.invoice_no = validated_data.get('invoice_no', instance.invoice_no)
        instance.doc_no = validated_data.get('doc_no', instance.doc_no)
        instance.customer = validated_data.get('customer', instance.customer)
        instance.branch = validated_data.get('branch', instance.branch)
        instance.status = validated_data.get('status', instance.status)
        instance.narration = validated_data.get('narration', instance.narration)
        instance.date = validated_data.get('date', instance.date)
        instance.total_amount = validated_data.get('total_amount', instance.total_amount)
        instance.discount = validated_data.get('discount', instance.discount)
        instance.grant_total = validated_data.get('grant_total', instance.grant_total)

        instance.save()
        keep_choices = []
        for choice in child:
            if "id" in choice.keys():
                if ChildInvoice.objects.filter(id=choice["id"]).exists():
                    c = ChildInvoice.objects.get(id=choice["id"])
                    c.item = choice.get('item', c.item)
                    c.price = choice.get('price', c.price)
                    c.quantity = choice.get('quantity', c.quantity)
                    c.sub_total = choice.get('sub_total', c.sub_total)

                    c.save()
                    keep_choices.append(c.id)
                else:
                    continue
            else:
                c = ChildInvoice.objects.create(**choice, key=instance)
                keep_choices.append(c.id)
        print(instance.child,'///////////////////////////')
        for choice in instance.child:
            if choice.id not in keep_choices:
                choice.delete()

        return instance
class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = "__all__"


class JournalItemSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    class Meta:
        model = JournalItem
        fields = [
        'id','journal_entry',
        'account','partner',
        'debit_amount','credit_amount'
        ]
        read_only_fields = ('journal_entry',)


class JournalEntrySerializer(serializers.ModelSerializer):
    journal_item = JournalItemSerializer(many=True)

    class Meta:
        model = JournalEntry
        fields = ('id','date','transaction_type','description','journal_item')

    def create(self, validated_data):
        albums_data = validated_data.pop('journal_item')
        musician = JournalEntry.objects.create(**validated_data)
        for album_data in albums_data:
            JournalItem.objects.create(journal_entry=musician, **album_data)
        return musician

    def update(self, instance, validated_data):
        journal_item = validated_data.pop('journal_item')
        # albums = (instance.child).all()
        # albums = list(albums)
        instance.date = validated_data.get('date', instance.date)
        instance.transaction_type = validated_data.get('transaction_type', instance.transaction_type)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        keep_choices = []
        for choice in journal_item:
            if "id" in choice.keys():
                if JournalItem.objects.filter(id=choice["id"]).exists():
                    c = JournalItem.objects.get(id=choice["id"])
                    c.account = choice.get('account', c.account)
                    c.partner = choice.get('partner', c.partner)
                    c.debit_amount = choice.get('debit_amount', c.debit_amount)
                    c.credit_amount = choice.get('credit_amount', c.credit_amount)
                    c.save()
                    keep_choices.append(c.id)
                else:
                    continue
            else:
                c = JournalItem.objects.create(**choice, journal_entry=instance)
                keep_choices.append(c.id)
        for choice in instance.journal_item:
            if choice.id not in keep_choices:
                choice.delete()

        return instance


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


class CustomerReceiptSerializer(WritableNestedModelSerializer):
    journal_entry = JournalEntrySerializer()
    # child = JournalItemSerializer(many=True)
    class Meta:
        model = CustomerReceipt
        # fields = ('reciept_no', 'journal_entry')
        fields = "__all__"


class ExpenseCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpenseCategory
        fields = "__all__"


class ExpenseSerializer(WritableNestedModelSerializer):
    journal_entry = JournalEntrySerializer()
    class Meta:
        model = Expenses
        fields = "__all__"

class ParantInvoiceSerializerTest(WritableNestedModelSerializer):
    journal_entry = JournalEntrySerializer()
    child = InvoiceLineSerializer(many=True)

    class Meta:
        model = SalesInvoice
        fields = "__all__"
