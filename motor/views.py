
# Create your views here.
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext

def home(request, saludo, opcion):
      return render_to_response('home.html', {'saludo': saludo, 'opcion':opcion},
                               context_instance=RequestContext(request))