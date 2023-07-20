from tir import Webapp
from resources.commons import data_atual, cria_sequencial_alfanumerico
import unittest

class MATA020(unittest.TestCase):

	# Cadastro de fornecedor

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup("SIGACOM",data_atual(),"99","01","02")
		inst.oHelper.Program("MATA020")
	
	def test_MATA020_001(self):
		self.oHelper.SetButton("Incluir")
		self.oHelper.SetValue("A2_COD",cria_sequencial_alfanumerico())
		self.oHelper.SetValue("A2_LOJA","01")
		self.oHelper.SetValue("A2_NOME","PHARMA FORMULA MANUPULADOS")
		self.oHelper.SetValue("A2_NREDUZ","PHARMA FORMULA")
		self.oHelper.SetValue("A2_END","RUA DUQUE DE CAXIAS")
		self.oHelper.SetValue("A2_BAIRRO","CENTRO")
		self.oHelper.SetValue("A2_EST","PB")
		#self.oHelper.SetValue("A2_COD_MUN","")
		self.oHelper.SetValue("A2_MUN","JOAO PESSOA")
		self.oHelper.SetValue("A2_CEP","58000-000")
		self.oHelper.SetValue("A2_TIPO", "J - Juridico")
		#Inscrição estadual
		#self.oHelper.SetValue("A2_INSCR","")
		self.oHelper.SetValue("A2_CGC","36.975.606/0001-90")
		self.oHelper.SetValue("A2_EMAIL","PHAMAFORMULATST@GMAIL.COM")
		self.oHelper.ClickFolder("Outros")
		self.oHelper.SetValue("A2_FABRICA", "1 - Sim")
		self.oHelper.SetValue("A2_CODLOC","")
		self.oHelper.ClickFolder("Cadastrais")
		self.oHelper.SetButton("Confirmar")
		self.oHelper.SetButton("Fechar")

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()