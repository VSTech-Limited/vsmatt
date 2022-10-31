from rest_framework import serializers
from shop.models import BusinessProfile, BusinessBranch
from core.models import BusinessCategory


class BusinessBranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessBranch
        fields = ['name', 'slug', 'business', 'latitude', 'longitude', 'address']


class BusinessCategorySerializer(serializers.ModelSerializer):
    businesses = BusinessBranchSerializer(many=True, read_only=True)

    class Meta:
        model = BusinessCategory
        fields = ['title', 'slug', 'marker', 'businesses']
