from django.shortcuts import render
from django.core.mail import send_mail
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from .models import Solicitud, TipoSolicitud, Tema, TipoTema
from .forms import SolicitudForm, TemaForm
from django.db.models import Q


# Create your views here.
'''
def index(request):
    send_mail('Se ha registrado una solicitud',
    'Solicitud registrada.Gracias por tu tiempo, estamos atendiendo tu solicitud',
    'jonhatan.zelada@gmail.com',
    ['hsuarez@onp.gob.pe'],
    fail_silently=False)
    return render(request,'send/enviado.html')
'''

class CrearSolicitudView(CreateView):
    model = Solicitud
    template_name = 'solicitud/nueva_solicitud.html'
    form_class = SolicitudForm
    #return render(request,'solicitud/confirmacion.html')
    success_url = reverse_lazy('confirmacion')

class SolicitudListView(ListView):
    queryset = Solicitud.objects.filter(Q(estado='creado'))
    model = Solicitud
    #THe nest is a session variable who wil be call from hmtl
    context_object_name = 'solicitudes_pen'
 
class CrearTemaView(CreateView):
    model = Tema
    template_name = 'solicitud/nuevo_tema.html'
    form_class = TemaForm
    success_url = reverse_lazy('confirmacion_tema')

class TemaListView(ListView):
     queryset = Tema.objects.all
     model = Tema
     context_object_name = 'temas_nuevos'
     template_name = 'solicitud/tema_list.html'

def confirmado(request):
    return render(request,'solicitud/confirmacion.html')

def confirma_tema(request):
    return render(request,'solicitud/confirmacion_tema.html')

def load_solicitud(request):
    tipo_id=request.GET.get('tipo')
    solicitudes = Solicitud.objects.filter(tipo_id=tipo_id)
    return render(request,'solicitud/solicitud_dropdown_list_options.html',{'solicitudes':solicitudes})

def home(request):
    return render(request,'index.html')

def capacitacion(request):
    return render(request,'capacitacion.html')

def beneficios(request):
    return render(request,'beneficios.html')

def actividades(request):
    return render(request,'actividades.html')
    
def promociones(request):
    return render(request,'promociones.html')

def matricula(request):
    return render(request,'matricula.html')
    
def preguntas(request):
    return render(request,'preguntas.html')
    
def confirm_insc(request):
    return render(request,'confirmacion_inscr.html')