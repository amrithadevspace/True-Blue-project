
from django.shortcuts import render
from temp.models import Reading
from openai import OpenAI
import os

def reading(request):
    obj = Reading.objects.all()
    context = {
        'ii': obj
    }
    return render(request, 'reading/view.html', context)


def post(request, idd):
    obj = Reading.objects.first()
    result = None

    if request.method == "POST":
        ph = request.POST.get("PH")
        turbidity = request.POST.get("TURBIDITY")
        temperature = request.POST.get("TEMPERATURE")
        tds = request.POST.get("TDS")
        alkalinity = request.POST.get("ALKALINITY")
        chloride = request.POST.get("CHLORIDE")

        prompt = f"""
        Existing Sensor Readings:
        pH: {obj.ph}
        Turbidity: {obj.turbidity}
        Temperature: {obj.temperature}

        User Entered Readings:
        TDS: {tds}
        Alkalinity: {alkalinity}
        Chloride: {chloride}

        Based on all these water parameters, classify the water quality as:
        Good, Moderate, or Poor. Also give a one-line reason.
        """

        client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )

        result = response.choices[0].message.content

    context = {
        'i': obj,
        'result': result
    }
    return render(request, "reading/upload.html", context)


from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def reading_api(request):
    obj = Reading.objects.all().values()
    return Response({"data": list(obj)})


@api_view(['POST'])
def reading_post_api(request, idd):
    obj = Reading.objects.get(reading_id=idd)

    ph = request.data.get("PH")
    turbidity = request.data.get("TURBIDITY")
    temperature = request.data.get("TEMPERATURE")
    tds = request.data.get("TDS")
    alkalinity = request.data.get("ALKALINITY")
    chloride = request.data.get("CHLORIDE")

    prompt = f"""
    Existing Sensor Readings:
    pH: {obj.ph}
    Turbidity: {obj.turbidity}
    Temperature: {obj.temperature}

    User Entered Readings:
    TDS: {tds}
    Alkalinity: {alkalinity}
    Chloride: {chloride}

    Based on all these water parameters, classify the water quality as:
    Good, Moderate, or Poor. Also give a one-line reason.
    """

    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    result = response.choices[0].message.content

    return Response({"result": result})
