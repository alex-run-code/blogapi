
from django.urls import path, include
from . import views
import rest_framework
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'posts', views.PostViewSet)
router.register(r'users', views.UserViewSet)


urlpatterns = [
   path('', include(router.urls)),
]
