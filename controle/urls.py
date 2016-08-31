from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'example.views.home', name='home'),
	url(r'^dashboard/$',views.dash,name='dash'),
	url(r'^dashboard/medicamentos/$',views.medicamento,name='medicamentos'),
	url(r'^dashboard/medicamentos/vencidos/$',views.medVenc,name='medicamentosVencidos'),
	url(r'^dashboard/medicamentos/alterar/$',views.medicamentoAlt,name='medicamentosAlt'),
	url(r'^dashboard/fornecedores/$',views.fornecedor,name='fornecedores'),
	url(r'^dashboard/fornecedores/alterar/$',views.fornecedorAlt,name='fornecedoresAlt'),
	url(r'^dashboard/clientes/$',views.cliente,name='clientes'),
	url(r'^dashboard/clientes/alterar/$',views.clienteAlt,name='clientesAlt'),
	url(r'^dashboard/lotes/$',views.lote,name='lotes'),
	url(r'^dashboard/lotes/alterar/$',views.loteAlt,name='lotesAlt'),
	url(r'^dashboard/entradaesaida/$',views.entradaSaida,name='EntradaESaida'),
	url(r'^dashboard/entradaesaida/visualizar/(?P<medicamento_id>\d+)/$',views.visEntSai,name='EntradaESaidaVisulizarEsp')

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
