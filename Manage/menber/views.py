from django.shortcuts import render
from django.template import loader,Context
from django.http import HttpResponse
from Manage.menber.models import Menbers
from django.shortcuts import render_to_response

# Create your views here.

def Menber(request):
    menber = Menbers.objects.all()
    t = loader.get_template('menber.html')
    c = Context({'menber':menber})
    return HttpResponse(t.render(c))

def Index(request):
    return render_to_response("index.html",{})

def search_form(request):
    return render_to_response('search_form.html')

def search(request):
    if 'q' in request.GET and request.GET['q']:
         q = request.GET['q']
         menber = Menbers.objects.filter( menber_name=q)
         return render_to_response('search_results.html',
                                   {'menber':menber,'query':q})
    else:
        return HttpResponse('Please submit a search term.')
