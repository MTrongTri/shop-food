from django.urls import path

from products import views as product_views

urlpatterns = [
    path('create', product_views.product_create),
    path('list', product_views.product_list),
    path('<uuid:id>/edit/', product_views.product_edit, name='product_edit'),
    path('<uuid:id>/delete/', product_views.product_delete, name='product_delete'),
]
