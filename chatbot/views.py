from django.shortcuts import render
import os
from groq import Groq


def chatbot(request):
    context = {'res': ""}

    if request.method == "POST":
        chat = request.POST.get('Chatbot')
        res = chat_with_gpt(chat)
        context = {'res': res}

    return render(request, 'chatbot/Chatbot.html', context)


def chatbot_tech(request):
    context = {'res': ""}

    if request.method == "POST":
        chat = request.POST.get('Chatbot')
        res = chat_with_gpt(chat)
        context = {'res': res}

    return render(request, 'chatbot/Chatbot_tech.html', context)


def chat_with_gpt(prompt):
    try:
        api_key = os.getenv("GROQ_API_KEY")

        if not api_key:
            return "Groq API key is not configured."

        client = Groq(api_key=api_key)

        response = client.chat.completions.create(
            model="openai/gpt-oss-120b",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=2000,
            temperature=0.7,
        )

        return response.choices[0].message.content.strip()

    except Exception as e:
        return f"An error occurred: {e}"