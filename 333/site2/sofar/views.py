from django.shortcuts import render

from django.http import HttpResponse, HttpResponsePermanentRedirect, JsonResponse
from .models import posts, modelsEncoder


# Create your views here.
def index(request):
    return render(request,"sofar/index.html")

def postsofar(request): #Получение id с формы
    id_q = request.POST.get("id_q",0)
    if id_q !='0':
        id_q =int(id_q)
        if id_q > 0:
            data=("ID", int(id_q))
            return HttpResponsePermanentRedirect (f"/sofarid?ID="+str(id_q)+"&name=tp/") 



def getdatasofar(request): #Получение информации по id
    id_q =int(request.GET.get("ID"))
    if id_q > 0:
        post=posts.objects.get(id=id_q)
    return JsonResponse(post, safe=False, encoder=modelsEncoder)
                                     
  