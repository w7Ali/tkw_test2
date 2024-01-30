from django.urls import path
from home.views import task2

urlpatterns = [
    path('home/', task2),
]
