from django.db import models
from django.core.serializers.json import DjangoJSONEncoder

# Create your models here.
class posts(models.Model): #����� � ������������
    title = models.CharField(max_length=30)#���������
    bycreator = models.CharField(max_length=30)#�����
    views = models.IntegerField(default=0)#���������
    position = models.PositiveIntegerField(default=id)#�������
    

class modelsEncoder(DjangoJSONEncoder):# ������������ �������
    def default(self, obj):
        if isinstance(obj, posts):
            return {"ID": obj.id,"position":obj.position ,"Avtor":obj.bycreator, "title":obj.title, "views":obj.views}
        return super().default(obj)
            