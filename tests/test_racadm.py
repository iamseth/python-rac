import racadm
import unittest

TEST_HOST = 'localhost'
TEST_USERNAME = 'admin'
TEST_PASSWORD = 'password123'

class TestRAC(unittest.TestCase):

    def setUp(self):
        self.rac = racadm.RAC(TEST_HOST, TEST_USERNAME, TEST_PASSWORD)

    def test_inject_header(self):
        req = self.rac._inject_header('')
        self.assertTrue(req == "<?xml version='1.0'?>")

    def test_extract_sid(self):
        sid = self.rac._extract_sid('<SID>1234</SID>')
        self.assertTrue(sid, '1234')

    def test_extract_cmd_output(self):
        sid = self.rac._extract_cmd_output('<CMDOUTPUT>success</CMDOUTPUT>')
        self.assertTrue(sid, 'success')

if __name__ == '__main__':
    unittest.main()
