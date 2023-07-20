import unittest
from tests.sigacom.AGRA045TESTCASE import AGRA045

suite = unittest.TestSuite()
suite.addTest(AGRA045('test_AGRA045_001'))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)