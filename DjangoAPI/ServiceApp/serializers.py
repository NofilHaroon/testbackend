from rest_framework import serializers
from ServiceApp.models import Service, Listing, Vendor

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = (
                'ServiceID',
                'ServiceName'
                )

class ListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = (
                'ListingId',
                'Category',
                'Title',
                'Rating',
                'Description',
                'Thumbnail',
                'Img_one',
                'Img_two',
                'Img_three'
                )

class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = (
                'VendorId',
                'VendorName',
                'Contact',
                'Profilepic'
                )