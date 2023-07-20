import unittest
from tests.sigacom.MATA020TESTCASE import MATA020

suite = unittest.TestSuite()
suite.addTest(MATA020('test_MATA020_001'))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)