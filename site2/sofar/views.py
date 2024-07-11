from django.shortcuts import render

from django.http import HttpResponse, HttpResponsePermanentRedirect, JsonResponse
from .models import posts, modelsEncoder
import requests

from rest_framework.test import RequestsClient
#, TicketCase


# Create your views here.
def index(request):
    return render(request,"sofar/index.html")

def postsofar(request): #Получение id с формы
    #params = {'key1': 'value1', 'key2': 'value2','key3': 'value3','key4': 'value4','key5': 'value5','key6': 'value6'}
    #cookies = {'session_id': '123456789'}
    id_q = request.POST.get("id_q",0)
    #client = RequestsClient()
    #url = f'http://www.farpost.ru/vladivostok/service/construction/guard/+/Системы+видеонаблюдения/'
    #response = client.get(url)
    #response = requests.get(url,params=params, cookies=cookies)
    #res = response.objects.all()[0:40]
    #f = open("test.txt", "w")
    #for i in range(1, 200):
    #    d=response.objects.get(id=i)
    #    dd='key1'+d.key1+'key2'+d.key2+'key3'+d.key3+'key4'+d.key4+'key5'+d.key5+'key6'+d.key6
    #    #"ID": obj.id,
   
        
    #response = requests.get(url)
    #print(response)
    #
    #
    #response_on_python = response.json()
    #return HttpResponse(response)
    #return HttpResponse(response)
    

    if id_q !='0':
        id_q =int(id_q)
        if id_q > 0:
            data=("ID", int(id_q))
            
            # return HttpResponse(TicketCase)
            return HttpResponsePermanentRedirect (f"/sofarid?ID="+str(id_q)+"&name=tp/") 



def getdatasofar(request): #Получение информации по id
    id_q =int(request.GET.get("ID"))
    if id_q > 0:
        post=posts.objects.get(id=id_q)
    return JsonResponse(post, safe=False, encoder=modelsEncoder)
                                     
  