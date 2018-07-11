from decimal import Decimal

from django.shortcuts import render

# Create your views here.
from pwdj.galeria.models import Model


def index(request):
    ctx = {
        'galeria':
            [
                Model('Social media now takes a back seat in favor of ‘new sets of tools’ to solve problems.',
                      Decimal('400.00'),
                      'We need people like you, and we need people not like you,” she told the audience.'),
                Model('Social media now takes a back seat',
                      Decimal('7000.00'),
                      'We need people like you, and we need people not like you,” she told the audience.'),
                Model('New sets of tools’ to solve problems.',
                      Decimal('8600.00'),
                      'She told the audience.')
             ]
    }
    return render(request, 'galeria/index.html', context=ctx)
