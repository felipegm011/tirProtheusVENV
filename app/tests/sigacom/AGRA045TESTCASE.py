from tir import Webapp
from resources.commons import data_atual, cria_sequencial_alfanumerico
import unittest

class AGRA045(unittest.TestCase):

	# cadastro locais de estoque

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup("SIGACOM",data_atual(),"99","01","02")
		inst.oHelper.Program("AGRA045")

	# inclusão
	def test_AGRA045_001(self):
		self.oHelper.SetButton("Incluir")
		self.oHelper.SetValue("NNR_CODIGO",cria_sequencial_alfanumerico())
		self.oHelper.SetValue("NNR_DESCRI","")
		self.oHelper.SetValue("NNR_CODIGO","02")
		self.oHelper.SetValue("NNR_DESCRI","ARMAZEM 02 TESTE")
		self.oHelper.SetValue("NNR_TIPO", "1 - Padrão")
		self.oHelper.SetButton("Confirmar")
		self.oHelper.SetButton("Fechar")
		
	
	# alteração
	def test_AGRA045_002(self):
		self.oHelper.SetButton("Alterar")
		self.oHelper.SetValue("Usuário","000000",  grid = True, row = 1, grid_number = 2)
		self.oHelper.SetValue("Descrição","Administrador",  grid = True, row = 1, grid_number = 2)
		self.oHelper.LoadGrid()
		self.oHelper.SetButton("Confirmar")
		self.oHelper.SetButton("Fechar")
	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()