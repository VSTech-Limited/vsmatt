from django.shortcuts import render
from rest_framework import generics
from .serializers import BusinessSerializer
from shop.models import BusinessProfile


# Create your views here.


class BusinessesView(generics.ListAPIView):
    serializer_class = BusinessSerializer
    queryset = BusinessProfile.objects.all()
