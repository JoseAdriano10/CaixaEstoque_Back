from django.contrib import admin
from .models import UnidadeMedida, Ambiente, Secao, Localizacao, Grupo, SubGrupo, Produto

# Register your models here.

admin.site.register(UnidadeMedida),
admin.site.register(Ambiente),
admin.site.register(Secao),
admin.site.register(Localizacao),
admin.site.register(Grupo),
admin.site.register(SubGrupo),
admin.site.register(Produto),
