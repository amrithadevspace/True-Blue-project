from django.shortcuts import render
from temp.models import Reading
# Create your views here.
def home(request):
    return render(request,'temp/home.html')
def user(request):
    return render(request,'temp/user.html')
def admin(request):
    return render(request,'temp/admin.html')
def technician(request):
    return render(request,'temp/technician.html')
def upload(request):
    obj = Reading.objects.all()
    context = {
        'feed': obj
    }
    return render(request,'temp/upload.html',context)
