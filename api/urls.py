from django.urls import path
from . import views

urlpatterns = [
    path('businesses/', views.BusinessesView.as_view(), name='businesses')
]
