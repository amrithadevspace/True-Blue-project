from django.shortcuts import render, redirect
from django.http import HttpResponse
from login.models import Login
from technecian_register.models import Technecian


# def login(request):
#
#     if request.method == "POST":
#
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#
#         try:
#
#             obj = Login.objects.get(username=username,password=password)
#
#             request.session['u_id'] = obj.u_id
#
#             # ADMIN LOGIN
#             if obj.type == "admin":
#
#                 return redirect('/temp/admin/')
#
#
#             # TECHNICIAN LOGIN
#             elif obj.type == "technician":
#
#                 tech = Technecian.objects.get(technecian_id=obj.u_id)
#
#                 if tech.status == "Accepted":
#
#                     request.session['u_id'] = tech.technecian_id
#
#                     return redirect('/temp/technician/')
#
#                 elif tech.status == "Pending":
#
#                     return HttpResponse("Admin approval pending")
#
#                 elif tech.status == "Rejected":
#
#                     return HttpResponse("Registration rejected")
#             # USER LOGIN
#             elif obj.type == "user":
#
#                 return redirect('/temp/user/')
#         except:
#             return HttpResponse("Incorrect username or password")
#     return render(request,'login/login.html')

def login(request):

    if request.method == "POST":

        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            obj = Login.objects.get(username=username,password=password)

            request.session['u_id'] = obj.u_id

            if obj.type == "admin":
                return redirect('/temp/admin/')

            elif obj.type == "technician":

                tech = Technecian.objects.get(technecian_id=obj.u_id)

                if tech.status == "Accepted":
                    request.session['u_id'] = tech.technecian_id
                    return redirect('/temp/technician/')

                elif tech.status == "pending":
                    return render(request,'login/login.html',{'msg':'Admin approval pending'})

                elif tech.status == "Rejected":
                    return render(request,'login/login.html',{'msg':'Registration rejected'})

            elif obj.type == "user":
                return redirect('/temp/user/')

        except:
            return render(request,'login/login.html',{'msg':'Incorrect username or password'})

    return render(request,'login/login.html')

from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import android_serializer
class login_app(APIView):

    def get(self,request):
        obj = Login.objects.all()
        ser = android_serializer(obj,many=True)
        return Response(ser.data)

    def post(self,request):

        username = request.data['username']
        password = request.data['password']

        obj = Login.objects.filter(username=username,password=password)

        ser = android_serializer(obj,many=True)

        return Response(ser.data)