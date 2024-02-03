from django.urls import path
from .views import CartViewSet,OrderView,SingleOrderView

urlpatterns = [
    path('cart/', CartViewSet.as_view({'get':'list', 'post':'create', 'patch':'create', 'put':'create', 'delete':'destroy',})),
    path('order/', OrderView.as_view()),
    path('order/<int:pk>/', SingleOrderView.as_view()),
]