from rest_framework import serializers,fields
from Debit_Note.models import (
        DebitNote
        )
from rest_framework.validators import UniqueTogetherValidator
from drf_writable_nested import WritableNestedModelSerializer

# from invoice import test
# from invoice import serializers
from Journal_Entry.serializers import (
    JournalItemSerializer,JournalEntrySerializer
)

from collections import OrderedDict



class DebitNoteSerializer(WritableNestedModelSerializer):
    journal_entry = JournalEntrySerializer()


    class Meta:
        model = DebitNote
        fields = "__all__"
