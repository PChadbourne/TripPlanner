# TripPlanner
Trip Planner python script for iTrellis programming challenge

Domain: Trip Calculator
Interface: Native GUI
Language: Python

# How To Run
Run as you would any other python script. Open a commandline in the directory and enter "python tripPlanner.py"

Optionally include either "test" or a filename as a commandline argument to run the testing suite or calculate expenses on a different file.
For example "python tripPlanner.py test" or "python tripPlanner.py complexExpenses"

# Creating an Expense Sheet
Expense sheets should be plain text without a file extension.
They should be of format of space seperated decimal values on multiple lines.
Each line represents an individual student's expenses.

The following is an example expense sheet:

```
33.15 27.99 18.82

12.56 24.95 16.50

20.00 10.00 5.00
```

Where the first student, Amy, had expenses of $33.15, $27.99, and $18.82
Expense sheets can support up to 26 students, and each student is named alphabetically:

```
"Amy", "Brian", "Charlie", "David", "Emma",
"Frank", "Gina", "Howard", "Isabelle", "Josh",
"Karen", "Liam", "Mia", "Nathan", "Olivia",
"Patrick", "Quinn", "Ryan", "Susan", "Tom",
"Uma", "Victor", "Wanda", "Xavier", "Yara", "Zack"
```

# Additional Details

So as to avoid requiring payments of fractions of pennies, each transaction is only accurate to within the cent.
It is possible for there to be discrepencies of up to N cents, where N is the number of students involved.
This will always take the form of one student not having to repay up-to N cents.
No student will ever be required to pay more than the calculated average.
