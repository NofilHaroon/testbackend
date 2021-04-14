from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.core.files.storage import default_storage

from ServiceApp.models import Service, Listing, Vendor
from ServiceApp.serializers import ServiceSerializer, ListingSerializer, VendorSerializer

# Create your views here.

@csrf_exempt
def serviceApi(request, id=0):
    if request.method == 'GET':
        services = Service.objects.all()
        service_serializer = ServiceSerializer(services, many=True)
        return JsonResponse(service_serializer.data, safe=False)
    
    elif request.method == 'POST':
        service_data = JSONParser().parse(request)
        service_serializer = ServiceSerializer(data=service_data)
        if service_serializer.is_valid():
            service_serializer.save()
            return JsonResponse("Added Successfully!", safe=False)
        return JsonResponse("Failed to Add.", safe=False)

    elif request.method == 'PUT':
        service_data = JSONParser().parse(request)
        service = Service.objects.get(ServiceID=service_data['ServiceID'])
        service_serializer = ServiceSerializer(service, data=service_data)
        if service_serializer.is_valid():
            service_serializer.save()
            return JsonResponse("Updated Successfully!", safe=False)
        return JsonResponse("Failed to Update.", safe=False)
    
    elif request.method == 'DELETE':
        service = Service.objects.get(ServiceID=id)
        service.delete()
        return JsonResponse("Deleted Successfully.", safe=False)


@csrf_exempt
def listingApi(request, id=0):
    if request.method=='GET':
        listing = Listing.objects.all()
        listing_serializer = ListingSerializer(listing, many=True)
        return JsonResponse(listing_serializer.data, safe=False)

    elif request.method=='POST':
        listing_data=JSONParser().parse(request)
        listing_serializer = ListingSerializer(data=listing_data)
        if listing_serializer.is_valid():
            listing_serializer.save()
            return JsonResponse("Added Successfully!!" , safe=False)
        return JsonResponse("Failed to Add.",safe=False)
    
    elif request.method=='PUT':
        listing_data = JSONParser().parse(request)
        listing = Listing.objects.get(ListingId=listing_data['ListingId'])
        listing_serializer = ListingSerializer(listing, data=listing_data)
        if listing_serializer.is_valid():
            listing_serializer.save()
            return JsonResponse("Updated Successfully!!", safe=False)
        return JsonResponse("Failed to Update.", safe=False)

    elif request.method=='DELETE':
        listing=Listing.objects.get(ListingId=id)
        listing.delete()
        return JsonResponse("Deleted Succeffully!!", safe=False)

@csrf_exempt
def SaveFile(request):
    file=request.FILES['uploadedFile']
    file_name = default_storage.save(file.name,file)

    return JsonResponse(file_name,safe=False)

@csrf_exempt
def vendorApi(request, id=0):
    if request.method=='GET':
        vendor = Vendor.objects.all()
        vendor_serializer = VendorSerializer(vendor, many=True)
        return JsonResponse(vendor_serializer.data, safe=False)

    elif request.method=='POST':
        vendor_data=JSONParser().parse(request)
        vendor_serializer = VendorSerializer(data=vendor_data)
        if vendor_serializer.is_valid():
            vendor_serializer.save()
            return JsonResponse("Added Successfully!!" , safe=False)
        return JsonResponse("Failed to Add.",safe=False)
    
    elif request.method=='PUT':
        vendor_data = JSONParser().parse(request)
        vendor = Vendor.objects.get(VendorId=vendor_data['VendorId'])
        vendor_serializer = VendorSerializer(vendor, data=vendor_data)
        if vendor_serializer.is_valid():
            vendor_serializer.save()
            return JsonResponse("Updated Successfully!!", safe=False)
        return JsonResponse("Failed to Update.", safe=False)

    elif request.method=='DELETE':
        vendor=Vendor.objects.get(VendorId=id)
        vendor.delete()
        return JsonResponse("Deleted Succeffully!!", safe=False)