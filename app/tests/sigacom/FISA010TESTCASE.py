from tir import Webapp
from resources.commons import data_atual
import unittest

class FISA010(unittest.TestCase):

	# cadastro de municipios

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup("SIGACOM",data_atual(),"99","01","02")
		inst.oHelper.Program("FISA010")
	
	# inclusão
	def test_FISA010_001(self):
		self.oHelper.SetButton("Incluir")
		self.oHelper.SetValue("CC2_EST","PB")
		self.oHelper.SetValue("CC2_CODMUN","12346")
		self.oHelper.SetValue("CC2_MUN","MUNICIPIO TESTE 2")
		self.oHelper.SetButton("Confirmar")
		self.oHelper.SetButton("Fechar")

	# alteração
	def test_FISA010_002(self):
		self.oHelper.SetButton("Alterar")
		self.oHelper.SetValue("CC2_MUN","MUNICIPIO TESTE ALTERAÇÃO 2")
		self.oHelper.SetButton("Confirmar")
		self.oHelper.SetButton("Fechar")
	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()