from rest_framework import serializers,fields
from core.models import (
        Partner,Branch,Area,
        Product,ProductCategory,
        JournalEntry,Account,JournalItem,
        # ChildInvoice,Parent,
        InvoiceLineOld,
        InvoiceLine,
        SalesInvoice,
        SalesInvoiceNu,
        AccountDefault,CustomerReceipt,
        ExpenseCategory,Expenses,
        YearCharts,
        ExpenseYearChart,
        CreditNote,
        CreditNoteNumber
        )
from rest_framework.validators import UniqueTogetherValidator
from drf_writable_nested import WritableNestedModelSerializer

from invoice import test
# from invoice import serializers

from collections import OrderedDict

class CreditNoteNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreditNoteNumber
        fields = "__all__"

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

# class ChildInvoiceSerializer(serializers.ModelSerializer):
#     id = serializers.IntegerField(required=False)
#
#     class Meta:
#         model = ChildInvoice
#         fields = [
#             'id',
#             'key',
#             'item','price','quantity','sub_total'
#         ]
#         read_only_fields = ('key',)
#         # depth = 1

class InvoiceLineOldSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvoiceLineOld
        fields = "__all__"

class InvoiceLineSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvoiceLine
        fields = "__all__"


# class ParentInvoiceSerializer(serializers.ModelSerializer):
#     child = ChildInvoiceSerializer(many=True)
#
#     class Meta:
#         model = Parent
#         fields = [
#             "id",
#             'invoice_no', 'doc_no',
#             'customer', 'branch', 'status',
#             'narration', 'date', 'total_amount',
#             'discount', 'grant_total',
#             'journal_entry',
#             "child",
#         ]
#         # read_only_fields = ["tags"]
#     def create(self, validated_data):
#         journal_entry_instance = JournalEntry.objects.create(date=validated_data['date'],
#                                                              description=validated_data['narration'])
#        # #'transaction_type' will be "SALES" by default
#         # account_instance = Account.objects.create(name="some name")
#         account_instance = Account.objects.get(pk=1)
#        #
#         journal_item_instnce = JournalItem.objects.create(journal_entry=journal_entry_instance,
#                                                           account=account_instance,
#                                                           debit_amount=validated_data['total_amount'],
#                                                           credit_amount=validated_data['total_amount'])
#
#         child = validated_data.pop('child',[])
#         key = Parent.objects.create(journal_entry=journal_entry_instance, **validated_data)
#         # key = Parent.objects.create( **validated_data)
#
#         for choice in child:
#             ChildInvoice.objects.create(**choice, key=key)
#         return key
#
#     def update(self, instance, validated_data):
#         child = validated_data.pop('child')
#         instance.invoice_no = validated_data.get('invoice_no', instance.invoice_no)
#         instance.doc_no = validated_data.get('doc_no', instance.doc_no)
#         instance.customer = validated_data.get('customer', instance.customer)
#         instance.branch = validated_data.get('branch', instance.branch)
#         instance.status = validated_data.get('status', instance.status)
#         instance.narration = validated_data.get('narration', instance.narration)
#         instance.date = validated_data.get('date', instance.date)
#         instance.total_amount = validated_data.get('total_amount', instance.total_amount)
#         instance.discount = validated_data.get('discount', instance.discount)
#         instance.grant_total = validated_data.get('grant_total', instance.grant_total)
#
#         instance.save()
#         keep_choices = []
#         for choice in child:
#             if "id" in choice.keys():
#                 if ChildInvoice.objects.filter(id=choice["id"]).exists():
#                     c = ChildInvoice.objects.get(id=choice["id"])
#                     c.item = choice.get('item', c.item)
#                     c.price = choice.get('price', c.price)
#                     c.quantity = choice.get('quantity', c.quantity)
#                     c.sub_total = choice.get('sub_total', c.sub_total)
#
#                     c.save()
#                     keep_choices.append(c.id)
#                 else:
#                     continue
#             else:
#                 c = ChildInvoice.objects.create(**choice, key=instance)
#                 keep_choices.append(c.id)
#         print(instance.child,'///////////////////////////')
#         for choice in instance.child:
#             if choice.id not in keep_choices:
#                 choice.delete()
#
#         return instance
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
        # print(self,"self")
        print(validated_data,"validated_data")

        albums_data = validated_data.pop('journal_item')
        musician = JournalEntry.objects.create(**validated_data)
        for album_data in albums_data:
            print(album_data,'album_data')
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

class CreditNoteSerializer(WritableNestedModelSerializer):
    journal_entry = JournalEntrySerializer()


    class Meta:
        model = CreditNote
        fields = "__all__"
        # fields = ('id','Doc_no','Grand_total','Date','Comment','Partner','journal_entry')

    def create(self, validated_data):
        print(validated_data,"validated_data")
        var = test.test()

        validated_data['Doc_no'] = var
        print(var,"test")
        # journal_entry = validated_data.pop('journal_entry')
        # print(journal_entry,"journal_entry")
        # print(validated_data,"validated_data")
        #
        # orderedDict = OrderedDict(journal_entry)
        # entry_data = list(dict(orderedDict))
        # print(dict(orderedDict),'dictttttttttt')
        # # JournalEntrySerializer(data=dict(orderedDict))
        # jd_data = dict(orderedDict).pop('journal_item')
        # key = CreditNote.objects.create(**validated_data)
        # musician = JournalEntry.objects.create(**dict(orderedDict))
        #
        # for i_data in jd_data:
        #     print(i_data,'i_data')
        #     JournalItem.objects.create(journal_entry=musician, **album_data)

        # for item in orderedDict:
        #     print(item,'item')
        #     JournalEntry.objects.create(journal_entry=key,**item)
        return validated_data

        # creditnote = CreditNote.objects.create(**validated_data)
        # return creditnote

        # albums_data = validated_data.pop('journal_entry')
        # data = CreditNote.objects.create(**validated_data)
        # # for album_data in albums_data:
        # # journal_entry = validated_data['journal_entry']
        # print(albums_data,'journal_entry')



        # key = Parent.objects.create( **validated_data)
        # return key
    # def update(self, instance, validated_data):
    #     return validated_data
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
    child = InvoiceLineOldSerializer(many=True)

    class Meta:
        model = SalesInvoice
        fields = "__all__"

class ParantInvoiceSerializer(WritableNestedModelSerializer):
    journal_entry = JournalEntrySerializer()
    child = InvoiceLineSerializer(many=True)

    class Meta:
        model = SalesInvoiceNu
        fields = "__all__"




#  charts
class SalesPartnerChartSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesInvoice
        fields = ("customer","grant_total")

class SalesYearIncomeChartSerializer(serializers.ModelSerializer):
    class Meta:
        model = YearCharts
        fields = ('year',"grant_total")

class ExpenseYearChartSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpenseYearChart
        fields = ('year','grant_total')

class Expense_Cat_Vers_AmountChartSerializer(serializers.ModelSerializer):
    expense_Cat = serializers.CharField()
    amount = serializers.IntegerField()
    class Meta:
        # model = "__null__"
        fields = ('expense_Cat','amount')
