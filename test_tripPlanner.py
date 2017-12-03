# Unit tests for Trip Planner iTrellis programming challenge
#
# Run tripPlanner.py with commandline argument "test" to run
#
# Patrick Chadbourne, December 3rd, 2017

import unittest
import tripPlanner

class test_Read_File(unittest.TestCase):
    def test_Read_File(self):
        self.assertIsInstance(tripPlanner.readFile(), file, "readFile did not return a file")
        pass

class test_Parse_File(unittest.TestCase):
    def setUp(self):
        self.file = tripPlanner.readFile()
        pass

    def tearDown(self):
        pass

    def test_Parse_File(self):
        #len(tripPlanner.parseFile()) == 3 # Where 3 is the number of students (lines) in the expenses file
        self.assertTrue(len(tripPlanner.parseFile(self.file)) == 3, "parseFile did not parse the correct number of students")
        pass

class test_Parse_File_Contents(unittest.TestCase):
    def setUp(self):
        self.file = tripPlanner.readFile()
        pass

    def tearDown(self):
        pass

    def test_Parse_File(self):
        #len(tripPlanner.parseFile()) == 3 # Where 3 is the number of students (lines) in the expenses file
        self.assertTrue(len(tripPlanner.parseFile(self.file)) == 3, "parseFile did not parse the correct number of students")
        pass
