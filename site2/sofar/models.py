from django.db import models
from django.core.serializers.json import DjangoJSONEncoder
#from rest_framework.test import APITestCase
#from django.test import Client, APITestCase
#from django.core.urlresolvers import reverse
#from rest_framework import status
#from rest_framework.test import APITestCase

# Create your models here.
class posts(models.Model): #класс с объявлениями
    title = models.CharField(max_length=30)#Заголовок
    bycreator = models.CharField(max_length=30)#Автор
    views = models.IntegerField(default=0)#Просмотры
    position = models.PositiveIntegerField(default=id)#Позиция
    

class modelsEncoder(DjangoJSONEncoder):# Сериализация объекта
    def default(self, obj):
        if isinstance(obj, posts):
            return {"ID": obj.id,"position":obj.position ,"Avtor":obj.bycreator, "title":obj.title, "views":obj.views}
        return super().default(obj)
            

#class TicketCase(APITestCase):
 #   def test_user_details_on_ticket_id(self):
 #       response = self.client.get(f"https://www.farpost.ru/vladivostok/service/construction/guard/+/Системы+видеонаблюдения/")
  #      print(response.content) # this returns empty data in bytes