from django.urls import path
from .views import (
    ClienteListView,
    ClienteCreateView,
    ClienteDetailView,
    ClienteUpdateView,
    ClienteDeleteView,
)

app_name = 'clientes'

urlpatterns = [
    path('', ClienteListView.as_view(), name='cliente_list'),
    path('crear/', ClienteCreateView.as_view(), name='cliente_create'),
    path('<int:pk>/', ClienteDetailView.as_view(), name='cliente_detail'),
    path('<int:pk>/editar/', ClienteUpdateView.as_view(), name='cliente_update'),
    path('<int:pk>/eliminar/', ClienteDeleteView.as_view(), name='cliente_delete'),
]
