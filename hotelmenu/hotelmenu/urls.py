"""hotelmenu URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from foodmenu import views
from productapi.views import ProductsViews,ProductDetailView,ProductsModelViews,ProductDetailModelView,ProductViewSetView,ProductModelViewsetView,UserModelViewsetView
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register("api/v3/products",ProductViewSetView,basename="products")
router.register("api/v4/products",ProductModelViewsetView,basename="myproducts")
router.register("authenticate/v1/users",UserModelViewsetView,basename="Users")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hotelmenu/menu',views.DishViewItems.as_view()),
    path('hotelmenu/menu/<int:fno>',views.DishDetailView.as_view()),
    path("myg/products/",ProductsViews.as_view()),
    path("myg/products/<int:id>",ProductDetailView.as_view()),
    path("api/v2/myg/products",ProductsModelViews.as_view()),
    path("api/v2/myg/products/<int:id>",ProductDetailModelView.as_view())
]+router.urls
