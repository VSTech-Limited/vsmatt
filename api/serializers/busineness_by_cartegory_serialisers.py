from rest_framework import serializers

from business.models import BusinessBranch, BusinessCategory, BusinessProfile


class BusinessSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessProfile
        fields = ['name', 'slug', 'latitude', 'longitude', 'address']


class BusinessBranchSerializer(serializers.ModelSerializer):
    business = BusinessSerializer(read_only=True)
    class Meta:
        model = BusinessBranch
        fields = ['name', 'slug', 'business', 'latitude', 'longitude', 'address', 'customer_service_number']


class BusinessCategorySerializer(serializers.ModelSerializer):
    businesses = BusinessBranchSerializer(many=True, read_only=True)

    class Meta:
        model = BusinessCategory
        fields = ['title', 'slug', 'marker', 'businesses']
