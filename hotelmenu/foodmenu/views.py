from django.shortcuts import render

from foodmenu.models import menu_items
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class DishViewItems(APIView):
    def get(self,request,*args,**kwargs):

        return Response(data=menu_items)

    def post(self,request,*args,**kwargs):
        data=request.data
        menu_items.append(data)
        return Response(data=data)

class DishDetailView(APIView):
    def get(self,request,*args,**kwargs):
        fno=kwargs.get("fno")
        item=[item for item in menu_items if item["code"]==fno].pop()
        return Response(data=item)

    def put(self,request,*args,**kwargs):
        fno = kwargs.get("fno")
        item = [item for item in menu_items if item["code"] == fno].pop()
        item.update(request.data)
        return Response(data=item)

    def delete(self,request,*args,**kwargs):
        fno = kwargs.get("fno")
        item = [item for item in menu_items if item["code"] == fno].pop()
        menu_items.remove(item)
        return Response(data=item)


