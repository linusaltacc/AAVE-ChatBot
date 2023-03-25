from django.shortcuts import render
from .models import *
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import openai
from chat.apikey import openai_api_key
def chat(request):
    chats = Chat.objects.all()
    return render(request, 'chat.html', {
        'chats': chats,
    })

@csrf_exempt
def Ajax(request):
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        text = request.POST.get('text')
        openai.api_key = openai_api_key
        res = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": "You are a Aave chatbot! You are here to help users learn more about Aave and answer any questions they may have. Whether they're new to DeFi or a seasoned crypto enthusiast, You are here to assist them. You should not mention about ChatGPT or any other resources other than questions related to aave. Answer the following question. "+text,}
        ]
        )
        response = res.choices[0].message["content"]
        chat = Chat.objects.create(
            text = text,
            gpt = response
        )

        return JsonResponse({'data': response,})
    return JsonResponse({})