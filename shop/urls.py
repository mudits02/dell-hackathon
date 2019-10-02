from django.urls import path
from shop.views import (
    product_list,
    product_detail,
    service_page,
    support_page,
    service_purchased
)

app_name = 'shop'

urlpatterns = [
    path('', product_list, name='product_list'),
    path('<slug:category_slug>/', product_list,
         name='product_list_by_category'),
    path('<int:id>/<slug:slug>/', product_detail,
         name='product_detail'),
    path('services', service_page, name='service_page'),
    path('supports', support_page, name='support_page'),
    path('service/purchased/', service_purchased, name='service_purchased'),
]
