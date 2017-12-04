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

    def test_Parse_File(self):
        #len(tripPlanner.parseFile()) == 3 # Where 3 is the number of students (lines) in the expenses file
        self.assertTrue(len(tripPlanner.parseFile(self.file)) == 3, "parseFile did not parse the correct number of students")
        pass

class test_Parse_File_Content(unittest.TestCase):
    def setUp(self):
        self.file = tripPlanner.readFile()
        pass

    def test_Parse_File_Content(self):
        self.assertIsInstance(tripPlanner.parseFile(self.file)[0][0], float, "parseFile did not return a nested list of floats")
        pass

class test_Calculate_Total_Expenses(unittest.TestCase):
    def setUp(self):
        self.file = tripPlanner.readFile()
        self.expenses = tripPlanner.parseFile(self.file)
        pass

    def test_Calculate_Total_Expenses(self):
        self.assertTrue(len(tripPlanner.calculateTotalExpenses(self.expenses)) == 3, "calculateTotalExpenses did not calculate for the correct number of students")
        self.assertIsInstance(tripPlanner.calculateTotalExpenses(self.expenses)[0], float, "calculateTotalExpenses did not return a list of floats")
        pass

class test_Calculate_Average_Expense(unittest.TestCase):
    def setUp(self):
        self.file = tripPlanner.readFile()
        self.expenses = tripPlanner.parseFile(self.file)
        self.totalExpenses = tripPlanner.calculateTotalExpenses(self.expenses)
        pass

    def test_Calculate_Average_Expense(self):
        #tripPlanner.calculateAverageExpense(self.totalExpenses) == 44.87 # Where 44.87 is the expected value for the given test file
        self.assertTrue(tripPlanner.calculateAverageExpense(self.totalExpenses) == 44.87, "calculateAverageExpense did not calculate the correct average")
        pass

class test_Calculate_Differences(unittest.TestCase):
    def setUp(self):
        self.file = tripPlanner.readFile()
        self.expenses = tripPlanner.parseFile(self.file)
        self.totalExpenses = tripPlanner.calculateTotalExpenses(self.expenses)
        self.averageExpense = tripPlanner.calculateAverageExpense(self.totalExpenses)
        pass

    def test_Calculate_Differences(self):
        #tripPlanner.calculateDifferences(self.averageExpense, self.totalExpenses)[2] == 31.55 # Where 31.55 is the expected value for the given test file and student
        self.assertTrue(tripPlanner.calculateDifferences(self.averageExpense, self.totalExpenses)[2] == 31.55, "calculateDifferences did not calculate the expected value")
        self.assertTrue(len(tripPlanner.calculateDifferences(self.averageExpense, self.totalExpenses)) == 3, "calculateDifferences did not calculate the expected number of values")
        pass
