"""newhotel URL Configuration

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
from dishesapi.views import DishesViews,DishesDetailViews,DishesModelViews,DishesDetailModelView,DishesViewsetView,DishesModelViewSetView,UserModelViewsetView
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register("dishapi/v3/restaurant/dishes",DishesViewsetView,basename="dishes")
router.register("dishapi/v4/dishes",DishesModelViewSetView,basename="mydishes")
router.register("authenticate/v1/users",UserModelViewsetView,basename="user")
urlpatterns = [
    path('admin/', admin.site.urls),
    path('restaurant/dishes',DishesViews.as_view()),
    path('restaurant/dishes/<int:id>',DishesDetailViews.as_view()),
    path("dishapi/v2/restaurant/dishes",DishesModelViews.as_view()),
    path("dishapi/v2/restaurant/dishes/<int:id>",DishesDetailModelView.as_view())
]+router.urls
