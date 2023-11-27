import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _
class TurmaChoices(models.IntegerChoices):
    SEXTO = 1, '6° Ano'
    SETIMO = 2, '7° Ano'
    OITAVO = 3, '8° Ano'
    NONO = 4, '9° Ano'
    TODAS = 5, 'Todas'

class SistemasChoices(models.IntegerChoices):
    DIRETOR = 1, 'Diretor'
    PROFESSOR = 2, 'Professor'

class User(models.Model):
    nome = models.CharField(_("Nome"), blank=False, max_length=50,)
    cpf = models.CharField(_("cpf"), blank=False, max_length=11, unique=True)
    matricula = models.CharField(_("Número Matricula"), blank=False, max_length=50,)
    email = models.EmailField(_("Email"), max_length=200, unique=True,)
    cargo = models.IntegerField(choices=SistemasChoices.choices, default=SistemasChoices.PROFESSOR)

    class Meta:    
        verbose_name = _('Usuario')
        verbose_name_plural = _('Usuarios')
        ordering = ['id']

    def __str__(self):
        return self.nome 
  
class Endereco(models.Model):
    cidade = models.CharField(_('Cidade'), max_length=200)
    cep = models.CharField(_('CEP'),)
    bairro = models.CharField(_('Bairro'), max_length=200)
    rua = models.CharField(_('Rua'), max_length=200)
    numero_casa = models.CharField(_('Número '),)
    endereco_cliente = models.ForeignKey(User, blank=True, default=None, null=True, on_delete= models.DO_NOTHING)

    class Meta:
        verbose_name = _('Endereço')
        verbose_name_plural = _('Endereços')

    
    def __str__(self):
        return f"Cidade: {self.cidade} | Bairro: {self.bairro} | Rua: {self.rua}"

class Postagem(models.Model):
    assunto = models.CharField(_("Assunto"), max_length=50)
    data = models.DateTimeField(_("Data da postagem"), blank=False)
    conteudo = models.TextField(_("Sobre a postagem"), max_length=500)
    turma = models.IntegerField(choices=TurmaChoices.choices, default=TurmaChoices.TODAS)
    responsavel = models.ForeignKey(User, blank=True, default=None, null=True, on_delete= models.DO_NOTHING)

