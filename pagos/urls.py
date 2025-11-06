from django.urls import path
from .views import PagosListView, PagosCreateView, PagosUpdateView, PagosDeleteView, PagosDetailView   


urlpatterns = [
    path('', PagosListView.as_view(), name='lista_pagos'),
    path('crear/', PagosCreateView.as_view(), name='crear_pago'),
    path('editar/<int:pk>/', PagosUpdateView.as_view(), name='editar_pago'),
    path('borrar/<int:pk>/', PagosDeleteView.as_view(), name='borrar_pago'),
    path('<int:pk>/', PagosDetailView.as_view(), name='detalle_pago'),
]


