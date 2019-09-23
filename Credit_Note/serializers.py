from rest_framework import serializers,fields
from Credit_Note.models import (
        CreditNote,
        CreditNoteNumber
        )
from rest_framework.validators import UniqueTogetherValidator
from drf_writable_nested import WritableNestedModelSerializer

# from invoice import test
# from invoice import serializers
from Journal_Entry.serializers import (
    JournalItemSerializer,JournalEntrySerializer
)

from collections import OrderedDict




class CreditNoteNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreditNoteNumber
        fields = "__all__"

class CreditNoteSerializer(WritableNestedModelSerializer):
    journal_entry = JournalEntrySerializer()


    class Meta:
        model = CreditNote
        fields = "__all__"
