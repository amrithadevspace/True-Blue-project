from django.shortcuts import render
from user_register.models import User
from login.models import Login
from django.http import  HttpResponseRedirect
from.serializers import android_serializer
# Create your views here.
def user_register(request):
    if request.method == 'POST':
        obj = User()
        obj.user_name = request.POST.get('username')
        obj.email_id = request.POST.get('emailid')
        obj.first_name = request.POST.get('FirstName')
        obj.last_name = request.POST.get('Lastname')
        obj.phon_no = request.POST.get('phoneno')
        obj.password = request.POST.get('password')
        # obj.status="pending"
        obj.save()

        ob = Login()
        ob.username= obj.user_name
        ob.password = obj.password
        ob.type = 'user'
        ob.u_id = obj.user_id
        ob.save()
        return HttpResponseRedirect('/login/login')
    return render(request, 'user_register/user register.html')
def view_user_register (request):
    ob=User.objects.all()
    context={
     'user':ob
    }
    return render(request, 'user_register/view manage user.html',context)

def delete(request,idd):
    obj=User.objects.get(user_id=idd)
    obj.delete()

    ob=Login.objects.get(u_id=idd,type='user')
    ob.delete()
    return view_user_register(request)

def reject(request,idd):
    obj=User.objects.get(user_id=idd)
    obj.status="rejected"
    obj.save()
    return view_user_register(request)

from django.http import HttpResponse
from rest_framework.views import APIView, Response


class user(APIView):
    def post(self, request):
        obj = User()
        obj.user_name = request.data['user_name']
        obj.email_id = request.data['email_id']
        obj.first_name = request.data['first_name']
        obj.last_name = request.data['last_name']
        obj.phon_no = request.data['phon_no']
        obj.password = request.data['password']
        # obj.status = "pending"
        obj.save()
        
        ob = Login()
        ob.username = obj.user_name
        ob.password = obj.password
        ob.type = 'user'
        ob.u_id = obj.user_id
        ob.save()

        return HttpResponse ('user')

class view_profile(APIView):
    def post(self,request):
        obj=User.objects.filter(user_id=request.data['abc'])
        print(len(obj))
        ser=android_serializer(obj,many=True)
        return Response(ser.data)
