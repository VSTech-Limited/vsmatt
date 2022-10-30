from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from shop.models import BusinessProfile
from .serializers.busineness_by_cartegory_serialisers import BusinessCategorySerializer
from .serializers.serializers import BusinessSerializer
from core.models import BusinessCategory


# Create your views here.


class BusinessesView(APIView):
    def get(self, request, slug=None):
        businesses = BusinessProfile.objects.all()
        serializer = BusinessSerializer(businesses, many=True)
        if slug:
            business = get_object_or_404(BusinessProfile, slug=slug)
            serializer = BusinessSerializer(business)
        return Response(serializer.data)


class BusinessByCategoryView(APIView):
    def get(self, request, category_slug=None):
        categories = BusinessCategory.objects.all()
        if category_slug:
            categories = BusinessCategory.objects.filter(slug=category_slug)
        serializer = BusinessCategorySerializer(categories, many=True)
        return Response(serializer.data)
