from rest_framework import serializers

from business.models import BusinessCategory, BusinessBranch, BusinessProfile


class BusinessCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessCategory
        fields = ['title', 'marker', 'slug']


class BranchSerializer(serializers.ModelSerializer):
    category = BusinessCategorySerializer(many=False, read_only=True)

    class Meta:
        model = BusinessBranch
        fields = ['name', 'slug', 'category', 'latitude', 'longitude', 'address']


class BusinessSerializer(serializers.ModelSerializer):
    branch = BranchSerializer(many=True, read_only=True)

    class Meta:
        model = BusinessProfile
        fields = ['name', 'slug', 'owner', 'latitude', 'longitude', 'address', 'branch']
