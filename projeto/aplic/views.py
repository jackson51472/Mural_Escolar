from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Card

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
       
        cards = Card.objects.all().order_by('turma')
        
        
        cards_por_turma = {}

       
        for card in cards:
            turma = card.turma
            if turma not in cards_por_turma:
                cards_por_turma[turma] = []
            cards_por_turma[turma].append(card)

        
        context['turmas'] = cards_por_turma.keys()
        context['cards_por_turma'] = cards_por_turma

        return context
