from rest_framework import serializers,fields
from Expenses.models import (
        ExpenseCategory,Expenses,
        )

from rest_framework.validators import UniqueTogetherValidator
from drf_writable_nested import WritableNestedModelSerializer
from Journal_Entry.serializers import (
    JournalItemSerializer,JournalEntrySerializer
)


class ExpenseCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpenseCategory
        fields = "__all__"


class ExpenseSerializer(WritableNestedModelSerializer):
    journal_entry = JournalEntrySerializer()
    class Meta:
        model = Expenses
        fields = "__all__"
