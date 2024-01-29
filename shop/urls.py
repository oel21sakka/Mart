from django.urls import path
from .views import CategoryView,ProductView,SingleCategoryView,SingleProductView

urlpatterns = [
    path('category/', CategoryView.as_view()),
    path('product/', ProductView.as_view(), name='product_view'),
    path('category/<slug:slug>', SingleCategoryView.as_view()),
    path('product/<slug:slug>', SingleProductView.as_view(), name='product_detail_view'),
]