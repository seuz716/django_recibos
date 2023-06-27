from django.contrib import admin
from .models import Cliente
from .forms import ClienteForm

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    form = ClienteForm
    list_display = ('codigo', 'nombre', 'nit_cc', 'email', 'direccion', 'telefono', 'pago', 'fecha')
    search_fields = ('nombre', 'nit_cc', 'email')
    list_filter = ('fecha',)
    date_hierarchy = 'fecha'
    readonly_fields = ('codigo',)
    prepopulated_fields = {'email': ('nombre',)}
    ordering = ('codigo',)
