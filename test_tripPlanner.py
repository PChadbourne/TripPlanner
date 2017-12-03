# Unit tests for Trip Planner iTrellis programming challenge
#
# Run tripPlanner.py with commandline argument "test" to run
#
# Patrick Chadbourne, December 3rd, 2017

import unittest
import tripPlanner

class test_Read_File(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_Testing_Working(self):
        self.assertIsInstance(tripPlanner.readFile(), str, "readFile did not return a string")
        pass
