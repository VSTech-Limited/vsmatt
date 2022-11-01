from rest_framework import serializers

from business.models import BusinessBranch, BusinessCategory


class BusinessBranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessBranch
        fields = ['name', 'slug', 'business', 'latitude', 'longitude', 'address']


class BusinessCategorySerializer(serializers.ModelSerializer):
    businesses = BusinessBranchSerializer(many=True, read_only=True)

    class Meta:
        model = BusinessCategory
        fields = ['title', 'slug', 'marker', 'businesses']
