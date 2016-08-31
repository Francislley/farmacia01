from django import forms
# Create your forms here

#models
from .models import Medicamento
from .models import Fornecedor
from .models import Cliente
from .models import Lote
from .models import Medicamento_Entrada
from .models import Medicamento_Saida
# formulário de medicamento
class MedicamentoForm(forms.ModelForm):

	class Meta:
		model = Medicamento
		fields = ['nome','descricao']

	def clean_nome(self):
		data = self.cleaned_data['nome']

		if len(data) <= 50:
			return data
		else:
			raise forms.ValidationError("Nome muito grande !!")

	def clean_descricao(self):
		data = self.cleaned_data['descricao']

		if len(data) <= 250:
			return data
		else:
			raise forms.ValidationError("Descrição muito grande !!")

#formulário de fornecedor
class FornecedorForm(forms.ModelForm):

	class Meta:
		model = Fornecedor
		fields = ['nome','contato']

	def clean_nome(self):
		data = self.cleaned_data['nome']

		if len(data) <= 40:
			return data
		else:
			raise forms.ValidationError("Nome muito grande !!")

	def clean_contato(self):
		data = self.cleaned_data['contato']

		if len(data) <= 40:
			return data
		else:
			raise forms.ValidationError("Contato muito grande !!")
# Cliente
class ClienteForm(forms.ModelForm):

	class Meta:
		model = Cliente
		fields = ['nome','contato']

	def clean_nome(self):
		data = self.cleaned_data['nome']

		if len(data) <= 40:
			return data
		else:
			raise forms.ValidationError("Nome muito grande !!")

	def clean_contato(self):
		data = self.cleaned_data['contato']

		if len(data) <= 40:
			return data
		else:
			raise forms.ValidationError("Contato muito grande !!")

#Lote
class LoteForm(forms.ModelForm):

	class Meta:
		model = Lote
		fields = ['fornecedor','numero','fabricacao','vencimento']

	def clean_numero(self):
		data = self.cleaned_data['numero']

		if len(data) <= 20:
			return data
		else:
			raise forms.ValidationError("Número de lote muito grande !!")

	def clean_fabricacao(self):
		data = self.cleaned_data['fabricacao']
		return data
	
	def clean_vencimento(self):
		data = self.cleaned_data['vencimento']
		return data

class Medicamento_EntradaForm(forms.ModelForm):

	class Meta:
		model = Medicamento_Entrada
		fields = ['usuario','medicamento','lote','quantidade']

	def clean_quantidade(self):

		data = self.cleaned_data['quantidade']

		if data >= 10000:
			raise forms.ValidationError("Quantidade Excedida")

		return data		
		
class Medicamento_SaidaForm(forms.ModelForm):

	class Meta:
		model = Medicamento_Saida
		fields = ['usuario','cliente','medicamento','quantidade']

	def clean_quantidade(self):

		data = self.cleaned_data['quantidade']

		if data >= 10000:
			raise forms.ValidationError("Quantidade Excedida")

		return data		
		
