from django.urls import path, include
from . import views

urlpatterns = [
    #path('enviomail', views.index,name='envio_mail'),
    path('add/', views.CrearSolicitudView.as_view(), name='add_solicitud'),
    path('add_tema/', views.CrearTemaView.as_view(), name='add_tema'),
    path('confi', views.confirmado, name='confirmacion'),
    path('confirmacion_tema', views.confirma_tema, name='confirmacion_tema'),
    path('lista/', views.SolicitudListView.as_view(), name='lista_solicitud'),
    path('lista_tema/', views.TemaListView.as_view(), name='lista_tema'),
    path('', views.home, name='gohome'),
    path('capacitacion', views.capacitacion, name='capacitacion'),
    path('beneficios', views.beneficios, name='beneficios'),
    path('actividades', views.actividades, name='actividades'),
    path('promociones', views.promociones, name='promociones'),
    path('matricula', views.matricula, name='matricula'),
    path('preguntas', views.preguntas, name='preguntas'),
    path('confirm_insc', views.confirm_insc, name='confirm_insc'),
]
