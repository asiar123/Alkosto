from django.urls import path
from home.views import index

urlpatterns = [
    path('listado_productos', index.as_view(),{'parametro_extra': 'Hola!'},name='listar_pacientes'),
]