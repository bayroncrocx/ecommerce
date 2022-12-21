from django.urls import path
from . import views


urlpatterns = [
 
    path('', views.inicio, name='inicio'),
    path('verform_categoria/', views.verform_categoria, name='verform_categoria'),
    path('crear_categoria', views.crear_categoria, name='crear_categoria'),
    path('verFormulario/', views.verFormulario, name='verFormulario'),
    path('crear_producto', views.crear_producto, name='crear_producto'),
    path('lista', views.lista, name='lista'),
    path('eliminar_producto/<str:product_name>', views.eliminar_producto, name='eliminar_producto'),
    path('editar_productos/<str:product_name>', views.editar_productos, name='editar_productos'),
    path('editar_productos/', views.editar_productos, name='prod'),

]