from django.contrib import admin
from .models import User, Endereco, Postagem

admin.site.register(Postagem)
class PostInline(admin.TabularInline):
    model = Postagem
    readonly_fields = ('id',)
    extra = 1
    classes = ('collapse', )
    list_display = ("assunto", "data", "turma", "responsavel",)

admin.site.register(Endereco)
class EnderecoInline(admin.TabularInline):
    model = Endereco
    readonly_fields = ('id',)
    extra = 1
    classes = ('collapse', )
    list_display = ("cidade", "cep", "rua", "bairro", "numero_casa",)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cpf', 'matricula', "cargo")
    inlines = [EnderecoInline, PostInline]
