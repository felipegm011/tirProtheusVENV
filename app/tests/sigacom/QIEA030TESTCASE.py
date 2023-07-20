from tir import Webapp
from resources.commons import data_atual, cria_sequencial_caracter
import unittest

class QIEA030(unittest.TestCase):

	# cadastro unidade de medida

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup("SIGACOM",data_atual(),"99","01","02")
		inst.oHelper.Program("QIEA030")

	# inclusão
	def test_QIEA030_001(self):
		self.oHelper.SetButton("Incluir")
		self.oHelper.SetValue("AH_UNIMED",cria_sequencial_caracter())
		self.oHelper.SetValue("AH_UMRES","TESTE")
		self.oHelper.SetValue("AH_DESCPO","TESTE CADASTRO NOVA UNIDADE DE MEDIDA")
		self.oHelper.SetButton("Confirmar")
		self.oHelper.SetButton("Fechar")

	# alteração
	def test_QIEA030_001(self):
		self.oHelper.SetButton("Alterar")
		self.oHelper.SetValue("AH_UMRES","TESTE")
		self.oHelper.SetValue("AH_DESCPO","TESTE CADSTRO NOVA UNID DE MEDIDA ALT 2")
		self.oHelper.SetValue("AH_DESCIN","RAÇÃO")
		self.oHelper.SetButton("Confirmar")
		self.oHelper.SetButton("Fechar")
	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()