#!/bin/python3

import unittest
import numpy as np
from turbojpeg import TurboJPEG
import time
jpeg = TurboJPEG()


class TestModule(unittest.TestCase):
    def test_module(self):

        # run assertion:
        self.assertEqual(1, 1)

    def test_encoding_processing_time(self):
        pass



if __name__ == '__main__':
    unittest.main()
