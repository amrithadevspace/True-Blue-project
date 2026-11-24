from django.shortcuts import render
from feedback.models import Feedback
# Create your views here.
def feedback(request):
    ss=request.session['u_id']
    if request.method=='POST':
        obj=Feedback()
        obj.user_id=ss
        obj.feedback=request.POST.get('feedback')
        obj.save()
    return render(request, 'feedback/feedback.html')
def view_feedback(request):
    ss = request.session['u_id']
    obj = Feedback.objects.filter(user_id=ss)
    context = {
        'feed': obj
    }

    return render(request,'feedback/view feedback.html',context)


from django.http import HttpResponse
from rest_framework.views import APIView, Response


class feed(APIView):
    def post(self, request):
        obj = Feedback()
        obj.user_id = request.data['abc']
        obj.feedback = request.data['feedback']
        obj.save()

        return HttpResponse('feed')


