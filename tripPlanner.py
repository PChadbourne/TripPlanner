# Trip Planner iTrellis programming challenge
# # # # # # # # # # # # # # # # # # # # # # # #
# Computes from a list of students and their
# personal expenses from the trip, the minimum
# amount of money that must change hands in
# order to equalize all the expenses.
#
# Input is taken from the expenses file, with
# each line representing a different student's
# expenses, seperated by whitespace.
# Up to 26 lines can be used in the file, hands
# each student will be assigned an alphabetical
# name from A-Z to maintain ease of use.
#
# Output is a printed string of required transactions
# necessary to balance the expenses of each student.
#
# Running the program with the commandline argument
# "test" will run the program's unit tests.
#
# Patrick Chadbourne, December 3rd, 2017

import unittest
import sys

def main():
    pass

def readFile():
    f = open('expenses', 'r')
    return f

def parseFile(file):
    parsedFile = []
    for line in file:
        expensesAsStrings = line.rstrip().split(" ")
        expensesAsFloats = []
        for value in expensesAsStrings:
            expensesAsFloats.append(float(value))
        parsedFile.append(expensesAsFloats)
    return parsedFile

def calculateTotalExpenses(individualExpenses):
    totalExpenses = []
    for student in individualExpenses:
        totalExpenses.append(sum(student))
    return totalExpenses

def calculateAverageExpense(totalledExpenses):
    total = sum(totalledExpenses) / len(totalledExpenses)
    total = round(total, 2)
    return total

def calculateDifferences(averageExpense, studentExpenses):
    differences = []
    for student in studentExpenses:
        differences.append(round(averageExpense - student, 2))
    return differences

def printTransactions():
    pass

def run_tests():
    loader = unittest.TestLoader()
    suite = loader.discover('.')

    runner = unittest.TextTestRunner()
    runner.run(suite)
    pass


if __name__ == '__main__':
    if 'test' in sys.argv[1:]:
        run_tests()
        sys.exit(0)
    else:
        main()
