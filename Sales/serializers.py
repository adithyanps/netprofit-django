from rest_framework import serializers,fields
from Sales.models import (
        InvoiceLine,
        SalesInvoice,
        )
from rest_framework.validators import UniqueTogetherValidator
from drf_writable_nested import WritableNestedModelSerializer

from Journal_Entry.serializers import (
    JournalItemSerializer,JournalEntrySerializer
)

class InvoiceLineSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvoiceLine
        fields = "__all__"

class SalesInvoiceSerializer(WritableNestedModelSerializer):
    journal_entry = JournalEntrySerializer()
    child = InvoiceLineSerializer(many=True)

    class Meta:
        model = SalesInvoice
        fields = "__all__"
