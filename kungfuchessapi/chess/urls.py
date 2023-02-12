from django.urls import path
from .views import chessEndPoint

urlpatterns = [
    path('', chessEndPoint.as_view())
]