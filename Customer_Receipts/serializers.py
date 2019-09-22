from rest_framework import serializers,fields
from Customer_Receipts.models import (
        CustomerReceipt
        )
from rest_framework.validators import UniqueTogetherValidator
from drf_writable_nested import WritableNestedModelSerializer

from Journal_Entry import serializers



class CustomerReceiptSerializer(WritableNestedModelSerializer):
    journal_entry = serializers.JournalEntrySerializer()
    # child = JournalItemSerializer(many=True)
    class Meta:
        model = CustomerReceipt
        # fields = ('reciept_no', 'journal_entry')
        fields = "__all__"
