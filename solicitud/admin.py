from django.contrib import admin
from .models import TipoSolicitud, Solicitud, Tema, TipoTema
# Register your models here.

##1.CHANGE VALUES ON MAIN PORTAL

admin.site.site_header = "Gestionate ONP"
admin.site.site_title = "Portal Gestionate"
admin.site.index_title = "Bienvenido al Portal Gestionate de la ONP"


##2.CHANGE VALUES ON EACH MODEL PAGE
class TipoSolicitudAdmin (admin.ModelAdmin):
    list_display = ('cod_tipo', 'nombre_solicitud', 'descripcion_tipo')    #fields to display
admin.site.register(TipoSolicitud,TipoSolicitudAdmin)


class SolicitudAdmin(admin.ModelAdmin):
    list_display = ('tipo', 'descripcion_sol', 'estado','solicitante', 'creada')    #fields to display
admin.site.register(Solicitud, SolicitudAdmin)



class TipoTemaAdmin(admin.ModelAdmin):
    list_display = ('cod_tipotema', 'nombre_tema', 'descripcion_tipotema')    #fields to display
admin.site.register(TipoTema, TipoTemaAdmin)

class TemaAdmin(admin.ModelAdmin):
    list_display = ('tipotema', 'descripcion_tema', 'fechatemacreada')    #fields to display
admin.site.register(Tema, TemaAdmin)


