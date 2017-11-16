# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import CreateView, ListView
from django.core.urlresolvers import reverse_lazy

from cadastro.models import Inscricao
from cadastro.forms import InscricaoForm


def home(request):
    return render(request, 'index.html')


class Criar(CreateView):
    model = Inscricao
    template_name = 'cadastro.html'
    sucess_url = reverse_lazy('lista')


class Lista(ListView):
    model = Inscricao
    template_name = 'lista.html'
    context_object = 'nome'
