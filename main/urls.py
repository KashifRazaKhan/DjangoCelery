from django.urls import path
from .views import index, failure_view

urlpatterns = [
    path('', index, name='index'),
    path('failure/', failure_view, name='failure'),
]