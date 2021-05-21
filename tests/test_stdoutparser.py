# -*- coding: utf-8 -*-

from .context import in2dp
from .mock_shellproxy import MockShellProxy

import unittest

class StdoutParserTestSuite(unittest.TestCase):

    def setUp(self):
        self.mockshell = MockShellProxy()
        self.parser = in2dp.StdoutParser()

    def test_parse_free_memory(self):
        '''Test parsing the stdout obtained from invoking the "free" shell command'''
        
        # stdout string returned from invoking the "free" sheel command
        stdout = self.mockshell.free_memory()

        # parse the stdout into a json object
        stats_json = self.parser.parse_free_memory(stdout)

        # assert equality with expected values
        self.assertEqual(stats_json['total'], 1026800)
        self.assertEqual(stats_json['used'], 198248)
        self.assertEqual(stats_json['free'], 828552)
        self.assertEqual(stats_json['shared'], 1068)
        self.assertEqual(stats_json['buffers'], 6952)
        self.assertEqual(stats_json['cached'], 71672)
        self.assertEqual(stats_json['used_minus_bufferscache'], 119624)
        self.assertEqual(stats_json['free_plus_bufferscache'], 907176)

if __name__ == '__main__':
    unittest.main()