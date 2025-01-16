from django.urls import path, include
from . import views
from django.views.generic import RedirectView
from django.contrib import admin

urlpatterns = [
    path('', views.index, name='index'),
    path('clientes/', views.cliente_list, name='cliente_list'),
    path('clientes/nuevo/', views.cliente_create, name='cliente_create'),
    path('clientes/editar/<int:pk>/', views.cliente_update, name='cliente_update'),
    path('clientes/eliminar/<int:pk>/', views.cliente_delete, name='cliente_delete'),
    path('tecnicos/', views.tecnico_list, name='tecnico_list'),
    path('tecnicos/nuevo/', views.tecnico_create, name='tecnico_create'),
    path('tecnicos/editar/<int:pk>/', views.tecnico_update, name='tecnico_update'),
    path('tecnicos/eliminar/<int:pk>/', views.tecnico_delete, name='tecnico_delete'),
    path('productos/', views.producto_list, name='producto_list'),
    path('productos/nuevo/', views.producto_create, name='producto_create'),
    path('productos/editar/<int:pk>/', views.producto_update, name='producto_update'),
    path('productos/eliminar/<int:pk>/', views.producto_delete, name='producto_delete'),
    path('partes/', views.parte_list, name='parte_list'),
    path('partes/nuevo/', views.parte_create, name='parte_create'),
    path('partes/editar/<int:pk>/', views.parte_update, name='parte_update'),
    path('partes/eliminar/<int:pk>/', views.parte_delete, name='parte_delete'),
    path('detalles/', views.detalleparte_list, name='detalleparte_list'),
    path('detalles/nuevo/', views.detalleparte_create, name='detalleparte_create'),
    path('detalles/editar/<int:pk>/', views.detalleparte_update, name='detalleparte_update'),
    path('detalles/eliminar/<int:pk>/', views.detalleparte_delete, name='detalleparte_delete'),
    path('partes/<int:parte_id>/materiales/nuevo/', views.detalleparte_add, name='detalleparte_add'),
    path('partes/materiales/eliminar/<int:pk>/', detalleparte_delete, name='detalleparte_delete'),
    path('', RedirectView.as_view(url='/login/', permanent=False)),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name 'registration/logged_out.html'), name='logout'),
    path('gestion/', include('gestion.urls')),
    path('admin/', admin.site.urls),




]

