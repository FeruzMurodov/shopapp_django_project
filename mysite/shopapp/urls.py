from django.urls import path

import shopapp.views
from .views import (
    ShopIndexView,
    GroupsListView,
    ProductsListView,
    OrdersListView,
    ProductCreateView,
    ProductDetailsView,
    OrdersDetailView,
    ProductUpdateView,
    ProductDeleteView,
    ProductsDataExportView,
)

app_name = 'shopapp'

urlpatterns = [
    path('', ShopIndexView.as_view(), name='index'),
    path("groups/", GroupsListView.as_view(), name='groups_list'),
    path("products/", ProductsListView.as_view(), name='products_list'),
    path("product/export/", ProductsDataExportView.as_view(), name='products-export'),
    path("products/create", ProductCreateView.as_view(), name='product_create'),
    path("products/<int:pk>/", ProductDetailsView.as_view(), name='product_details'),
    path("products/<int:pk>/update", ProductUpdateView.as_view(), name='product_update'),
    path("products/<int:pk>/archive", ProductDeleteView.as_view(), name='product_delete'),
    path("orders/", OrdersListView.as_view(), name='orders_list'),
    path("orders/<int:pk>/", OrdersDetailView.as_view(), name='order_details'),
]