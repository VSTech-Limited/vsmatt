from rest_framework import serializers
from products.models import Product
from business.models import BusinessBranch, BusinessCategory, BusinessProfile


class BusinessSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessProfile
        fields = ['name', 'slug', 'latitude', 'longitude', 'address']


class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'slug', 'price', 'image', 'updated']


class BusinessBranchSerializer(serializers.ModelSerializer):
    products = ProductsSerializer(many=True, read_only=True)
    business = BusinessSerializer(read_only=True)

    class Meta:
        model = BusinessBranch
        fields = ['name', 'slug', 'business', 'products', 'latitude', 'longitude', 'address', 'customer_service_number']


class BusinessCategorySerializer(serializers.ModelSerializer):
    businesses = BusinessBranchSerializer(many=True, read_only=True)

    class Meta:
        model = BusinessCategory
        fields = ['title', 'slug', 'marker', 'businesses']


# has no businesses
class BusinessCategoryMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessCategory
        fields = ['title', 'slug', 'marker']


class BusinessBranchSerializerWithCategory(serializers.ModelSerializer):
    products = ProductsSerializer(many=True, read_only=True)
    business = BusinessSerializer(read_only=True)
    category = BusinessCategoryMiniSerializer()

    class Meta:
        model = BusinessBranch
        fields = ['name', 'slug', 'business', 'category', 'products', 'latitude', 'longitude', 'address',
                  'customer_service_number']
