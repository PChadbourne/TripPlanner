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
# Running the program with any other commandline
# argument will try to find an expense file with
# the given name in the top-level directory.
#
# Patrick Chadbourne, December 3rd, 2017

import unittest
import sys

studentNames = [
"Amy", "Brian", "Charlie", "David", "Emma",
"Frank", "Gina", "Howard", "Isabelle", "Josh",
"Karen", "Liam", "Mia", "Nathan", "Olivia",
"Patrick", "Quinn", "Ryan", "Susan", "Tom",
"Uma", "Victor", "Wanda", "Xavier", "Yara", "Zack"
]

filename = "expenses"

def main():
    #Read the file containing the student's expenses
    f = readFile()
    #Parse the file to break it into a nested list of floats for easy handling
    individualExpenses = parseFile(f)
    #Total each student's expenses
    totalledExpenses = calculateTotalExpenses(individualExpenses)
    #Calculate the average expenditure
    averageExpense = calculateAverageExpense(totalledExpenses)
    #Calculate the difference between a student's spending and the average
    differencesInExpenditures = calculateDifferences(averageExpense, totalledExpenses)
    #Iterate through the differences and print the required transactions to even out
    printTransactions(differencesInExpenditures)
    sys.exit(0)

def readFile():
    try:
        f = open(filename, 'r')
    except IOError as err:
        print("Invalid argument interpretted as nonexistant file")
        print("Please remove the argument or fix the filename")
        sys.exit(1)
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

def getName(index):
    return studentNames[index]

def printTransactions(differences):
    #Iterates through the list of differences with x as the index of the value being given
    noTransactionsNeeded = True
    for x in range(len(differences)):
        while differences[x] > 0.0:
            noTransactionsNeeded = False
            giverName = getName(x)
            for y in range(len(differences)):
                #Iterates through the list of differences with y as the index of the value being received
                receiverName = getName(y)
                if differences[y] < 0.0 and abs(differences[y]) >= differences[x]:
                    #The recipient needs more or equal money to how much the giver owes
                    differences[y] = differences[y] + differences[x]
                    print(giverName + " must give " + '${:,.2f}'.format(differences[x]) + " to " + receiverName)
                    differences[x] = 0.0
                    break
                elif differences[y] < 0.0 and abs(differences[y]) < differences[x]:
                    #The recipient needs less money than the giver owes
                    differences[x] = differences[x] + differences[y]
                    print(giverName + " must give " + '${:,.2f}'.format(abs(differences[y])) + " to " + receiverName)
                    differences[y] = 0.0
                    continue
            break
    if noTransactionsNeeded:
        print("All student's expenses are equal.")
    return

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
        if len(sys.argv) >= 1:
            filename = sys.argv[1]
        main()
