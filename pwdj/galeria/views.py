from django.shortcuts import render

# Create your views here.
from pwdj.galeria.models import Model


def index(request):
    query_set = Model.objects.order_by('titulo')
    ctx = {
        'galeria': list(query_set)

    }
    return render(request, 'galeria/index.html', context=ctx)
