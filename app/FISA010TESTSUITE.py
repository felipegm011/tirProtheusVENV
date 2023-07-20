import unittest
from tests.sigacom.FISA010TESTCASE import FISA010

suite = unittest.TestSuite()
suite.addTest(FISA010('test_FISA010_001'))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)