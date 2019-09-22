from rest_framework import serializers,fields
from Journal_Entry.models import (
        JournalEntry,
        JournalItem,
        )
from rest_framework.validators import UniqueTogetherValidator
from drf_writable_nested import WritableNestedModelSerializer

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
