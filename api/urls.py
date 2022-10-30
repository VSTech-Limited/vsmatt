from django.urls import path
from . import views

urlpatterns = [
    path('businesses/<slug:slug>', views.BusinessesView.as_view(), name='business_detailed'),
    path('businesses/', views.BusinessesView.as_view(), name='businesses'),
    path('category/<slug:category_slug>', views.BusinessByCategoryView.as_view(), name='category_detailed'),
    path('category/', views.BusinessByCategoryView.as_view(), name='category'),
]
