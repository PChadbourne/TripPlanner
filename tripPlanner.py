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

def setString():
    return "Cow"

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
