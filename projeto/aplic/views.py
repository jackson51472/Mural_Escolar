from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Card

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Obtém todos os cards e os ordena pelo campo 'turma'
        cards = Card.objects.all().order_by('turma', 'data', 'hora')
        
        # Cria um dicionário para armazenar os cards por turma
        cards_por_turma = {}

        # Agrupa os cards por turma
        for card in cards:
            turma = card.turma
            if turma not in cards_por_turma:
                cards_por_turma[turma] = []
            cards_por_turma[turma].append(card)

        # Adiciona os dados ao contexto
        context['turmas'] = cards_por_turma.keys()
        context['cards_por_turma'] = cards_por_turma

        return context
