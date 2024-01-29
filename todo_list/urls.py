from django.conf.urls import include
from django.urls import path

from . import views
from .views import TodoList
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', TodoList, basename='todo')
urlpatterns = [
    path('api/', include(router.urls))
    # path('', TodoList.as_view({'get': 'list', 'post': 'create', 'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}))
]
