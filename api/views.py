from django.shortcuts import get_object_or_404, redirect
from rest_framework.response import Response
from rest_framework.views import APIView

from shop.models import BusinessProfile
from .serializers.busineness_by_cartegory_serialisers import BusinessCategorySerializer
from .serializers.serializers import BusinessSerializer
from core.models import BusinessCategory, ProductCategory


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
    def get(self, request, business_category_slug=None):
        categories = BusinessCategory.objects.all()
        if business_category_slug:
            categories = BusinessCategory.objects.filter(slug=business_category_slug)
        serializer = BusinessCategorySerializer(categories, many=True)
        return Response(serializer.data)


# needs improvement after the database schema has been updated
class BusinessByProductCategoryView(APIView):
    def get(self, request, product_category_slug=None):
        if not product_category_slug:
            return redirect('categories')
        product_category = get_object_or_404(ProductCategory, slug=product_category_slug)
        # get list of products that belong to the category provided
        category_products = product_category.product.all()
        # get the branches where the each products got above are sold are sold
        # [[branches for product 1], [branches for product 2], [branches for product n]]
        branches_products = [category_product.branch.all() for category_product in category_products]
        # go through branches groups to obtain distinct branches from different product to avoid
        # repetition of branch for multiple product that belong to same category and are sold in
        # one branch
        branches = set()
        for branch_list in branches_products:
            branches.update(set(branch_list))
        print(len(branches))
        categories = BusinessCategory.objects.filter(businesses__in=branches)
        serializer = BusinessCategorySerializer(categories, many=True)
        return Response(serializer.data)
