from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
# Create your views here.
from django.urls import reverse

from pwdj.galeria.models import Model


def index(request):
    query_set = Model.objects.order_by('titulo')
    ctx = {
        'galeria': list(query_set)

    }
    return render(request, 'galeria/index.html', context=ctx)


@login_required
def new(request):
    return render(request, 'galeria/galeria_form.html')


@login_required
def create(request):
    dct = request.GET
    preco = dct['preco'].replace(',', '.')
    model = Model(titulo=dct['titulo'], preco=preco, descricao=dct['descricao'])
    model.save()
    return redirect(reverse('galeria:index'))
