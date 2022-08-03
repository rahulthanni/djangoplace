from django.shortcuts import render

# Create your views here.
from ecomapi.models import products
from rest_framework.views import APIView
from rest_framework.response import Response


class ProductView(APIView):
    def get(self,request,*args,**kwargs):
        all_items=products

        if "price_lte" in request.query_params:
            price=int(request.query_params.get("price_lte"))
            all_items=[product for product in products if product["price"]<=price]
        if "limit" in request.query_params:
            limit=int(request.query_params.get("limit"))
            all_items=all_items[:limit]
        return Response(data=all_items)


    def post(self,request,*args,**kwargs):
        data=request.data
        products.append(data)
        return Response(data=data)

class ProductDetailView(APIView):

    def get(self,request,*args,**kwargs):
        proid=kwargs.get("proid")
        product=[product for product in products if product["id"]==proid].pop()
        return Response(data=product)

    def put(self,request,*args,**kwargs):
        proid = kwargs.get("proid")
        product = [product for product in products if product["id"] == proid].pop()
        product.update(request.data)
        return Response(data=product)

    def delete(self,request,*args,**kwargs):
        proid = kwargs.get("proid")
        product = [product for product in products if product["id"] == proid].pop()
        products.remove(product)
        return Response(data=product)