from django.shortcuts import render
from nearby_waterquality.models import NearbyWaterquality

# Create your views here.
def add_nearby(request):
    if request.method=='POST':
        obj=NearbyWaterquality()
        obj.place=request.POST.get('place')
        obj.ph=request.POST.get('ph')
        obj.save()
    return render(request,'nearby_waterquality/add_nearby_waterquality.html')

def view(request):
    vv=request.POST.get('lop')
    if request.method=='POST':
        ob = NearbyWaterquality.objects.filter(place=vv)
        context = {
            'nn': ob
        }
        return render(request,'nearby_waterquality/view_nearby.html',context)
    else:
        ob=NearbyWaterquality.objects.all()
        context={
            'nn':ob
        }
    return render(request,'nearby_waterquality/view_nearby.html',context)

def view_admin(request):
    vv=request.POST.get('lop')
    if request.method=='POST':
        ob = NearbyWaterquality.objects.filter(place=vv)
        context = {
            'nn': ob
        }
        return render(request,'nearby_waterquality/view_nearby_admin.html_',context)
    else:
        ob=NearbyWaterquality.objects.all()
        context={
            'nn':ob
        }
    return render(request,'nearby_waterquality/view_nearby_admin.html',context)

from django.http import HttpResponse
from rest_framework.views import APIView, Response
from .serializers import android_serializer

class nearby(APIView):
    def post(self, request):
        obj = NearbyWaterquality()
        obj.place=request.data['place']
        obj.ph=request.data['ph']
        obj.replay = 'pending'
        obj.save()

        return HttpResponse('nearby')


class viewnearby(APIView):
    def get(self,request):
        obj=NearbyWaterquality.objects.all()
        ser=android_serializer(obj,many=True)
        return Response(ser.data)