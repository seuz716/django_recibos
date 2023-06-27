from django.contrib import admin
from django.urls import path, include


app_name = 'clientes'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('clientes/', include('clientes.urls', namespace='clientes')),
]

