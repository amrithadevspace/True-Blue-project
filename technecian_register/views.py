from django.shortcuts import render
from technecian_register.models import Technecian
from login.models import Login
from django.http import HttpResponseRedirect
# Create your views here.
def technecian_register(request):

    if request.method == 'POST':
        obj = Technecian()
        obj.user_name = request.POST.get('username')
        obj.email_id = request.POST.get('emailid')
        obj.first_name = request.POST.get('FirstName')
        obj.last_name = request.POST.get('Lastname')
        obj.phone_no = request.POST.get('phoneno')
        obj.password = request.POST.get('password')
        obj.qulification=request.POST.get('qualification')
        obj.status="pending"
        obj.save()

        ob = Login()
        ob.username = obj.user_name
        ob.password = obj.password
        ob.type = 'technician'
        ob.u_id = obj.technecian_id
        ob.save()
        return HttpResponseRedirect('/login/login')
    return render(request,'technecian_register/technician register.html')


def view_technecian_register(request):
    obj = Technecian.objects.all()
    context = {
        'tec': obj
    }
    return render(request, 'technecian_register/view manage technecian.html',context)
def accept(request,idd):
    obj=Technecian.objects.get(technecian_id=idd)
    obj.status="Accepted"
    obj.save()
    return view_technecian_register(request)
def reject(request,idd):
    obj=Technecian.objects.get(technecian_id=idd)
    obj.status="Rejected"
    obj.save()
    return view_technecian_register(request)


from django.http import HttpResponse
from rest_framework.views import APIView, Response


class tech(APIView):
    def post(self, request):
        obj.user_name = request.data['username']
        obj.email_id = 1
        obj.first_name = request.data['FirstName']
        obj.last_name = request.data['Lastname']
        obj.phone_no = request.data['phoneno']
        obj.password = request.data['password']
        obj.qulification = request.data['qualification']
        obj.status = "pending"
        obj.save()

        return HttpResponse('tech')

