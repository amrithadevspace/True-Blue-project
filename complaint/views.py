from django.shortcuts import render
from complaint.models import Complaint
# Create your views here.
def complaint(request):
    ss=request.session['u_id']
    if request.method=='POST':
        obj=Complaint()
        obj.user_id=ss
        obj.replay='pending'
        obj.complaint=request.POST.get('complaint')
        obj.save()
    return render(request,'complaint/complaint.html')

def view_complaint(request):
    ss = request.session['u_id']
    obj=Complaint.objects.filter(user_id=ss)
    context={
        'comp':obj
    }
    return render(request,'complaint/view_complaint.html',context)


def view_complaint_admin(request):
    ss = request.session['u_id']
    obj=Complaint.objects.filter(user_id=ss)
    context={
        'comp':obj
    }
    return render(request,'complaint/view_complaint_admin.html',context)

def replay(request,idd):
    if request.method=='POST':
        obj=Complaint.objects.get(complaint_id=idd)
        obj.replay=request.POST.get('reply')
        obj.save()
        # return view_complaint(request)
    return render(request,'complaint/reply.html')

def replay_admin(request,idd):
    if request.method=='POST':
        obj=Complaint.objects.get(complaint_id=idd)
        obj.replay=request.POST.get('reply')
        obj.save()
        # return view_complaint(request)
    return render(request,'complaint/reply_admin.html')



def view_complaint_replay(request):
    ss = request.session['u_id']
    obj = Complaint.objects.filter(user_id=ss)
    context={
        "comp_reply":obj
    }

    return render(request,'complaint/view_complaint_replay.html',context)




from django.http import HttpResponse
from rest_framework.views import APIView,Response
from .serializers import android_serializer
class com(APIView):
    def post(self,request):
        obj=Complaint()
        obj.user_id=request.data['abc']
        obj.complaint=request.data['complaint']
        obj.replay='pending'
        obj.save()

        return HttpResponse('com')

class viewwreply(APIView):
    def post(self,request):
        obj=Complaint.objects.filter(user_id=request.data['abc'])
        ser=android_serializer(obj,many=True)
        return Response(ser.data)


















