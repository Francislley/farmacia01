from django.db import models
from django.contrib.auth.models import User

# Modelos
# class Usuario(models.Model):
# 	nome = models.CharField(max_length=50)
# 	login = models.CharField(max_length=50)
# 	# privilegio = models.CharField(max_length=100)
# 	senha = models.CharField(max_length=30)
#
# 	def __str__(self):
# 		return self.nome

class Fornecedor(models.Model):
	nome = models.CharField(max_length=40)
	contato = models.CharField(max_length=40)

	def __str__(self):
		return self.nome

class Lote(models.Model):
	fornecedor = models.ForeignKey(Fornecedor,on_delete=models.CASCADE)
	numero = models.CharField(unique=True,max_length=20)
	fabricacao = models.DateField(auto_now=False,auto_now_add=False)
	vencimento = models.DateField(auto_now=False,auto_now_add=False)

	def __str__(self):
		return self.numero


class Cliente(models.Model):
	nome = models.CharField(max_length=50)
	contato = models.CharField(max_length=40)

	def __str__(self):
		return self.nome


class Medicamento(models.Model):
	data_insercao = models.DateTimeField(auto_now=True)
	# cod_barra = models.CharField(max_length=100)
	nome = models.CharField(unique=True,max_length=50)
	descricao = models.CharField(max_length=250,blank=False)

	def __str__(self):
		return self.nome

class Medicamento_Entrada(models.Model):
	usuario = models.ForeignKey(User)
	medicamento = models.ForeignKey(Medicamento,on_delete=models.CASCADE)
	lote = models.ForeignKey(Lote,on_delete=models.CASCADE)
	data_entrada = models.DateTimeField(auto_now=False,auto_now_add=True)
	quantidade = models.IntegerField()


class Medicamento_Saida(models.Model):
	usuario = models.ForeignKey(User)
	medicamento = models.ForeignKey(Medicamento,on_delete=models.CASCADE)
	data_saida = models.DateTimeField(auto_now=False,auto_now_add=True)
	quantidade = models.IntegerField()
	cliente = models.ForeignKey(Cliente,on_delete=models.CASCADE)
