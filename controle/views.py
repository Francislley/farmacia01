from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,logout
from django.contrib.auth import login as auth_login
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# from .models import
from .models import Medicamento,Fornecedor,Cliente,Lote,Medicamento_Entrada,Medicamento_Saida
# forms
from .forms import MedicamentoForm,FornecedorForm,ClienteForm,LoteForm,Medicamento_EntradaForm,Medicamento_SaidaForm

#query
from django.db.models import Q

# #Inicial
# def principal(request):
# 	context = {
# 		'title':'Home'
# 	}
# 	return render(request,'home.html',context)


# Login

def login(request):
	context = {
		'title':'Login'
	}
	if request.user.is_authenticated():
		return redirect("controle/dashboard/")

	else:
		if request.method == "POST":
			user = authenticate(username=str(request.POST['username']),password=str(request.POST['password']))

			if user is not None:

		 		if user.is_active:

		 			auth_login(request, user)
		 			return redirect("controle/dashboard/")

			else:
				context['username'] = request.POST['username']
				context['error'] = "Usuário ou senha incorreto !!"
				context['classerror'] = "alert alert-warning"


	return render(request,'content/login.html',context)

# Dashboard do usuário
@login_required(login_url='/')
def dash(request):

	if request.GET.get('logout'):
		logout(request)
		return redirect("/")

	context = {
		'title':'Administrador'
	}
	return render(request,'content/dashboard.html',context)

# Medicamento
@login_required(login_url='/')
def medicamento(request):

	error = ""
	classerror = ""
	context = {}

	if request.method == "POST":

		form = MedicamentoForm(request.POST)

		if form.is_valid():

			form.save()
			classerror = "alert alert-success"
			error = "<h4>Cadastrado com sucesso !!</h3>"

		else:

			classerror = "alert alert-warning"
			context['nome'] = request.POST['nome']
			context['descricao'] = request.POST['descricao']

			error = "Campos inválidos <ul>"
			for i in form.errors:
				error += "<li>"+i.title()+"</li>"
			error += "</ul>"

	elif request.GET.get('deleta'):

		try:
			medD = Medicamento.objects.filter(pk=request.GET['deleta']).delete()
			classerror = "alert alert-success"
			error = "<h3>Deletado com sucesso !!</h3>"
		except:
			pass

	##
	if request.GET.get('busca'):
		b = request.GET['busca']
		medicamentos = Medicamento.objects.filter(Q(nome__contains=b)|Q(descricao__contains=b))
		if len(medicamentos) == 0:
			classerror = "alert alert-warning"
			error = "Nada Encontrado!!"
	else:
		medicamentos = Medicamento.objects.order_by('nome')

	page = request.GET.get('page')
	paginator =  Paginator(medicamentos,10)

	try:
		medicamentos = paginator.page(page)
	except PageNotAnInteger:
		medicamentos = paginator.page(1)
	except EmptyPage:
		medicamentos = paginator.page(paginator.num_pages)

	context['title'] = "Medicamentos"
	context['list_med'] = medicamentos
	context['error'] = error
	context['classerror'] = classerror

	return render(request,'content/medicamentos.html',context)

#medicamentos Alt
@login_required(login_url='/')
def medicamentoAlt(request):

	response = ""
	if request.method == "POST":
		form = MedicamentoForm(request.POST)

		if form.is_valid():

			medA = Medicamento.objects.filter(pk=request.POST['idAlt']).update(nome=request.POST['nome'],descricao=request.POST['descricao'])
			response = "Alterado"

		else:
			response = "<div class='alert alert-warning'>"
			response += "Campos inválidos <ul>"
			print(form.errors)
			for i in form.errors:
				response += "<li>"+i.title()+"</li>"
			response += "</ul></div>"

	return HttpResponse(response)

# Lotes
@login_required(login_url='/')
def lote(request):

	context = {'title':"Lotes",
			   'list_fon':Fornecedor.objects.order_by('nome')}
	error = ""
	classerror = ""

	if request.method =="POST":
		form = LoteForm(request.POST)

		if form.is_valid():
			form.save()
			classerror = "alert alert-success"
			error = "Cadastrado com sucesso !!"
		else:
			context['numero'] = request.POST['numero']
			context['fabricacao'] = request.POST['fabricacao']
			context['vencimento'] = request.POST['vencimento']
			classerror = "alert alert-warning"
			error = "Campos inválido <ul>"
			for i in form.errors:
				error += "<li>"+i+"</li>"

	elif request.GET.get('deleta'):
		entVer = Medicamento_Entrada.objects.filter(lote=request.GET['deleta'])
		if len(entVer)== 0:
			try:
				lotD = Lote.objects.get(pk=request.GET['deleta']).delete()
				classerror = "alert alert-success"
				error = "Deletado com sucesso !!"
			except:
				pass
		else:
			error = "Lote com entradas inseridas"
			classerror = "alert alert-warning"

	if request.GET.get('busca'):
		b = request.GET['busca']
		lotes = Lote.objects.filter(Q(numero__contains=b)|Q(fabricacao__contains=b)|Q(vencimento__contains=b))
	else:
		lotes = Lote.objects.order_by('vencimento')

	page = request.GET.get('page')
	paginator =  Paginator(lotes,10)

	try:
		lotes = paginator.page(page)
	except PageNotAnInteger:
		lotes = paginator.page(1)
	except EmptyPage:
		lotes = paginator.page(paginator.num_pages)

	context['list_lot'] = lotes
	context['error'] = error
	context['classerror'] = classerror
	return render(request,'content/lotes.html',context)

# Lotes Alt
@login_required(login_url='/')
def loteAlt(request):
	response = ""
	if request.method == "POST":

		form = LoteForm(request.POST)
		if form.is_valid():

			lotA = Lote.objects.filter(pk=request.POST['idAlt']).update(numero=request.POST['numero'],fornecedor=request.POST['fornecedor'],fabricacao=request.POST['fabricacao'],vencimento=request.POST['vencimento'])
			response = "Alterado"

		else:
			response = "<div class='alert alert-warning'>"
			response += "Campos inválidos <ul>"
			for i in form.errors:
				response += "<li>"+i.title()+"</li>"
			response += "</ul></div>"

	return HttpResponse(response)

# Fornecedor
@login_required(login_url='/')
def fornecedor(request):

	context = {}
	error = ""
	classerror = ""

	if request.method == "POST":
		form = FornecedorForm(request.POST)

		if form.is_valid():
			form.save()
			classerror = "alert alert-success"
			error = "<strong>Cadastrado com sucesso !!</strong>"
		else:
			context['nome'] = request.POST['nome']
			context['contato'] = request.POST['contato']
			classerror = "alert alert-warning"
			error = "Campos inválidos <ul>"
			for i in form.errors:
				error += "<li>"+i.title()+"</li>"
			error +="</ul>"

	elif request.GET.get('deleta'):

		try:
			fon = Fornecedor.objects.filter(pk=request.GET['deleta']).delete()
			error = "<strong>Deletado com sucesso !!</strong>"
			classerror = "alert alert-success"

		except:
			pass

	if request.GET.get('busca'):
		b = request.GET['busca'].strip()
		fornecedor = Fornecedor.objects.filter(Q(nome__contains=b)|Q(contato__contains=b))
		if len(fornecedor) == 0:
			classerror = "alert alert-warning"
			error = "Nada Encontrado!!"

	else:
		fornecedor = Fornecedor.objects.order_by('nome')


	page = request.GET.get('page')
	paginator =  Paginator(fornecedor,10)

	try:
		fornecedor = paginator.page(page)
	except PageNotAnInteger:
		fornecedor = paginator.page(1)
	except EmptyPage:
		fornecedor = paginator.page(paginator.num_pages)

	context['list_fon'] = fornecedor

	context['title'] = 'Fornecedor'
	context['list_fon'] = fornecedor
	context['error'] = error
	context['classerror'] = classerror

	return render(request,'content/fornecedor.html',context)

# fornecedor Alt
@login_required(login_url='/')
def fornecedorAlt(request):

	response = ""
	if request.method == "POST":
		form = FornecedorForm(request.POST)

		if form.is_valid():

			fonA = Fornecedor.objects.filter(pk=request.POST['idAlt']).update(nome=request.POST['nome'],contato=request.POST['contato'])
			response = "Alterado"

		else:
			response = "<div class='alert alert-warning'>"
			response += "Campos inválidos <ul>"
			for i in form.errors:
				response += "<li>"+i.title()+"</li>"
			response += "</ul></div>"

	return HttpResponse(response)

# clientes
@login_required(login_url='/')
def cliente(request):
	context = {}
	error = ""
	classerror = ""

	if request.method == "POST":
		form = ClienteForm(request.POST)

		if form.is_valid():
			form.save()
			classerror = "alert alert-success"
			error = "<strong>Cadastrado com sucesso !!</strong>"
		else:
			context['nome'] = request.POST['nome']
			context['contato'] = request.POST['contato']
			classerror = "alert alert-warning"
			error = "Campos inválidos <ul>"
			for i in form.errors:
				error += "<li>"+i.title()+"</li>"
			error +="</ul>"

	elif request.GET.get('deleta'):

		try:
			cli = Cliente.objects.filter(pk=request.GET['deleta']).delete()
			error = "<strong>Deletado com sucesso !!</strong>"
			classerror = "alert alert-success"

		except:
			pass

	if request.GET.get('busca'):
		b = request.GET['busca'].strip()
		cliente = Cliente.objects.filter(Q(nome__contains=b)|Q(contato__contains=b))
		if len(cliente) == 0:
			classerror = "alert alert-warning"
			error = "Nada Encontrado!!"

	else:
		cliente = Cliente.objects.order_by('nome')

	page = request.GET.get('page')
	paginator =  Paginator(cliente,10)

	try:
		cliente = paginator.page(page)
	except PageNotAnInteger:
		cliente = paginator.page(1)
	except EmptyPage:
		cliente = paginator.page(paginator.num_pages)

	context['list_cli'] = cliente
	context['title'] = 'Cliente'
	context['error'] = error
	context['classerror'] = classerror

	return render(request,'content/clientes.html',context)

# Cliente Alt
@login_required(login_url='/')
def clienteAlt(request):

	response = ""
	if request.method == "POST":
		form = ClienteForm(request.POST)

		if form.is_valid():

			cliA = Cliente.objects.filter(pk=request.POST['idAlt']).update(nome=request.POST['nome'],contato=request.POST['contato'])
			response = "Alterado"

		else:
			response = "<div class='alert alert-warning'>"
			response += "Campos inválidos <ul>"
			for i in form.errors:
				response += "<li>"+i.title()+"</li>"
			response += "</ul></div>"

	return HttpResponse(response)

#Entrada e saida de medicamentos
@login_required(login_url='/')
def entradaSaida(request):
	response = ""
	error = ""
	classerror = ""
	calcTot = lambda n:[i.quantidade for i in n]

	if request.POST.get('entrada') == "1":

		list_med_i = request.POST.getlist('medicamento')
		list_quant_i = request.POST.getlist('quantidade')
		print(list_med_i)
		print(list_quant_i)
		for i in range(len(list_med_i)):

			form = Medicamento_EntradaForm({'quantidade':list_quant_i[i],'medicamento':list_med_i[i],'lote':request.POST['lote'],'usuario':request.POST['usuario']})
			if form.is_valid():
				form.save()
				classerror = "alert alert-success"
				error = "<h4>Cadastrado com sucesso !!</h3>"
			else:
				error = "<div class='alert alert-warning'>"
				error += "Campos inválidos <ul>"
				for i in form.errors:
					error += "<li>"+i.title()+"</li>"
				error += "</ul></div>"



	# elif request.POST.get('saida'):
	# 	onta = Medicamento_Entrada.objects.filter(medicamento=)
	# 	pass
	elif request.POST.get('saida') == "1":

		ls_out_med = request.POST.getlist('medicamento')
		ls_out_qua = request.POST.getlist('quantidade')
		error = ""

		for i in range(len(ls_out_med)):

			medNomeGet = Medicamento.objects.get(pk=ls_out_med[i])
			qEntI = Medicamento_Entrada.objects.filter(medicamento=ls_out_med[i])
			totEntrada = sum(calcTot(Medicamento_Entrada.objects.filter(medicamento=ls_out_med[i])))
			totSaida = sum(calcTot(Medicamento_Saida.objects.filter(medicamento=ls_out_med[i])))
			status =  totEntrada - (totSaida + int(ls_out_qua[i]))
			print(status)
			if status<=0:

				error += "<div class='alert alert-warning'>"
				error += "Quantidade de saída indisponível ->"+str(medNomeGet)
				error += "</div><br>"

			else:
				form = Medicamento_SaidaForm({'medicamento':ls_out_med[i],'usuario':request.POST['usuario'],'cliente':request.POST['cliente'],'quantidade':ls_out_qua[i]})
				if form.is_valid():
					form.save()
					classerror = "alert alert-success"
					error = "<h4>Cadastrado com sucesso !!</h3>"
				else:
					error = "<div class='alert alert-warning'>"
					error += "Campos inválidos -> "+str(medNomeGet)+" <ul>"
					for i in form.errors:
						error += "<li>"+i.title()+"</li>"
					error += "</ul></div>"



	elif request.GET.get('deletaent'):

		try:
			qEnt = Medicamento_Entrada.objects.get(pk=request.GET['deletaent'])
			totEnt = sum(calcTot(Medicamento_Entrada.objects.filter(medicamento=qEnt.medicamento)))
			totSai = sum(calcTot(Medicamento_Saida.objects.filter(medicamento=qEnt.medicamento)))

			if totSai > (totEnt - qEnt.quantidade):
				error = "<h4>Não é possivel deletar pois as Saídas deste medicamento já foram contabilizadas !!</h4>"
				classerror = "alert alert-warning"
			else:
					qEnt.delete()
					error = "<strong>Deletado com sucesso !!</strong>"
					classerror = "alert alert-success"
		except:
			pass

	elif request.GET.get('deletasai'):

		try:
			sai = Medicamento_Saida.objects.filter(pk=request.GET['deletasai']).delete()
			error = "<h4>Deletado com sucesso !!</h4>"
			classerror = "alert alert-success"
		except:
			pass


	medEntrada = Medicamento_Entrada.objects.order_by('-data_entrada')
	medSaida = Medicamento_Saida.objects.order_by('-data_saida')
	med = Medicamento.objects.order_by('nome')
	lot = Lote.objects.order_by('fabricacao')
	cli = Cliente.objects.order_by('nome')

	estoque = []
	cont = 0
	for i in med:
		totEstE = sum(calcTot(Medicamento_Entrada.objects.filter(medicamento=i)))
		totEstS = sum(calcTot(Medicamento_Saida.objects.filter(medicamento=i)))
		estoque.append(totEstE - totEstS)
	# print(estoque)

	pageE = request.GET.get('pageent')
	pageS = request.GET.get('pagesai')
	pageG = request.GET.get('pageger')

	paginatorEnt = Paginator(medEntrada,10)
	paginatorSai = Paginator(medSaida,10)
	paginatorGer = Paginator(estoque,10)
	paginatorMed = Paginator(med,10)

	# entrada
	try:
		medEntrada = paginatorEnt.page(pageE)
	except PageNotAnInteger:
		medEntrada = paginatorEnt.page(1)
	except EmptyPage:
		medEntrada = paginatorEnt.page(paginatorEnt.num_pages)

	# saida
	try:
		medSaida = paginatorSai.page(pageS)
	except PageNotAnInteger:
		medSaida = paginatorSai.page(1)
	except EmptyPage:
		medSaida = paginatorSai.page(paginatorSai.num_pages)

	# estoque
	try:
		med = paginatorMed.page(pageG)
	except PageNotAnInteger:
		med = paginatorMed.page(1)
	except EmptyPage:
		med = paginatorMed.page(paginatorMed.num_pages)


	try:
		estoque = paginatorGer.page(pageG)
	except PageNotAnInteger:
		estoque = paginatorGer.page(1)
	except EmptyPage:
		estoque = paginatorGer.page(paginatorGer.num_pages)

	context = {
		'title':'Entrada e saída',
		'list_est':estoque,
		'list_ent':medEntrada,
		'list_sai':medSaida,
		'list_lot':lot,
		'list_med':med,
		'list_cli':cli,
		'error':error,
		'classerror':classerror
	}
	return render(request, 'content/entradasaida.html',context)


def visEntSai(request,medicamento_id):


	context = {
		'title':'Detalhes Medicamento',
	}
	return render(request, 'content/statusmedicamento.html',context)

def medVenc(request):
	error = ""
	classerror = ""

	from datetime import datetime
	lot = Lote.objects.filter(vencimento__lte=datetime.today())

	if request.GET.get('deletar'):

		entVer = Medicamento_Entrada.objects.filter(lote=request.GET['deleta'])
		if len(entVer)== 0:
			Lote.objects.filter(pk=request.GET['deletar']).delete()
			error = "Deletado com sucesso"
			classerror = "alert alert-success"
		else:
			error = "Lote com entradas inseridas"
			classerror = "alert alert-warning"
	elif request.GET.get('busca'):
		b = request.GET['busca']
		lot = Lote.objects.filter(numero__contains=b,vencimento__lte=datetime.today())

	pageE = request.GET.get('page')
	paginator = Paginator(lot,10)

	try:
		lotL = paginator.page(pageE)
	except PageNotAnInteger:
		lotL = paginator.page(1)
	except EmptyPage:
		lotL = paginator.page(paginator.num_pages)

	context = {
		'title':'Medicamentos Vencidos',
		'list_lotes':lotL,
		'error':error,
		'classerror':classerror,
	}

	return render(request, 'content/vencidos.html',context)

# Alteração de entrada
# @login_required(login_url='/')
# def entradaAlt(request):

# 	response = ""
# 	if request.method == "POST":

# 		if request.POST.get('lote'):
# 			form = Medicamento_EntradaForm(request.POST)

# 			if form.is_valid():

# 				cliA = Medicamento_Entrada.objects.filter(pk=request.POST['usuario']).update(lote=request.POST['lote'],quantidade=request.POST['quantidade'],medicamento=request.POST['medicamento'])
# 				response = "Alterado"

# 			else:
# 				response = "<div class='alert alert-warning'>"
# 				response += "Campos inválidos <ul>"
# 				for i in form.errors:
# 					response += "<li>"+i.title()+"</li>"
# 				response += "</ul></div>"

# 	return HttpResponse(response)
