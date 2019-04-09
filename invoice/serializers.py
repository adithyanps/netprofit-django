from rest_framework import serializers
from core.models import Customer,Branch,Item,C_Invoice,P_Invoice

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

class C_InvoiceSerializer(serializers.ModelSerializer):
    """child data of P_InvoiceSerializer"""

    class Meta:
        model = C_Invoice
        fields = ('id','key','item','price','quantity','sub_total')


class P_InvoiceSerializer(serializers.ModelSerializer):
    child = C_InvoiceSerializer(many=True)

    class Meta:
        model = P_Invoice
        fields = ('id','invoice_no','doc_no','customer','branch','status','narration','date','total_amount','discount','grant_total','child')

    def create(self, validated_data):
        albums_data = validated_data.pop('child')
        musician = P_Invoice.objects.create(**validated_data)
        for album_data in albums_data:
            C_Invoice.objects.create(key=musician, **album_data)
        return musician
#
    def update(self, instance, validated_data):
        albums_data = validated_data.pop('child')
        albums = (instance.child).all()
        albums = list(albums)
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
        # musician = P_Invoice.objects.update(**validated_data)

        # for album_data in albums_data:
            # C_Invoice.objects.update(key=musician, **album_data)

        for album_data in albums_data:
            album = albums.pop()
            album.item = album_data.get('item', album.item)
            album.price = album_data.get('price', album.price)
            album.quantity = album_data.get('quantity', album.quantity)
            album.sub_total = album_data.get('sub_total', album.sub_total)
        #
            album.save()
        
        return instance
