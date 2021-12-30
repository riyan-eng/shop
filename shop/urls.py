from django.contrib import admin
from django.urls import path, include
from dataQuery import Product

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('join/', include('join.urls')),
    path('api/products/', Product.dataProducts, name='dataProducts')
]
