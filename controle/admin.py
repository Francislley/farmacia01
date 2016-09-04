from django.contrib import admin
from .models import Usuario
from .models import Lote
from .models import Fornecedor
from .models import Cliente
from .models import Medicamento
from .models import Medicamento_Entrada
from .models import Medicamento_Saida
# Register your models here.

class UsuarioAdmin(admin.ModelAdmin):
	list_display = ['nome','login','senha']

# class FornecedorAdmin(admin.ModelAdmin):
# 	list_display = ['nome','contato']

# class LoteAdmin(admin.ModelAdmin):
# 	list_display = ['numero','fornecedor','fabricacao','vencimento']

# class ClienteAdmin(admin.ModelAdmin):
# 	list_display = ['nome','contato']

# class MedicamentoAdmin(admin.ModelAdmin):
# 	list_display = ['nome','data_insercao','descricao']

# class Medicamento_EntradaAdmin(admin.ModelAdmin):
# 	list_display = ['medicamento','lote','quantidade','data_entrada','usuario']

# class Medicamento_SaidaAdmin(admin.ModelAdmin):
# 	list_display = ['medicamento','quantidade','data_saida','usuario']


admin.site.register(Usuario,UsuarioAdmin)
# admin.site.register(Lote,LoteAdmin)
# admin.site.register(Fornecedor,FornecedorAdmin)
# admin.site.register(Cliente,ClienteAdmin)
# admin.site.register(Medicamento,MedicamentoAdmin)
# admin.site.register(Medicamento_Entrada,Medicamento_EntradaAdmin)
# admin.site.register(Medicamento_Saida,Medicamento_SaidaAdmin)