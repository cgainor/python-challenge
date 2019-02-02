## INSTRUCTIONS ##
# Given a set of financial data called budget_data.csv
# 2 columns: "Date" and "Profit/Losses"
# Create a python script that analyzes the records to calculate:
        # The total number of months in the dataset
        # The net total amount of "Profit/Losses" over the entire period
        # The average of the changes in "Profit/Losses" over the entire period
        # The greatest increase in profits (date and amount) over the entire period
        # The greatest decrease in losses (date and amount) over the entire period
    # Print analysis to terminal and export a text file with the results
# ---------------------------------------------------------------------------------
# Modules
import os
import csv

pyBank_csv = os.path.join("Resources","budget_data.csv")

# Open and read csv
with open(pyBank_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read the header row first
    csv_header = next(csvfile)

    # Initialize counting variables
    monthCount = 0
    netTotal = 0

    # Initialize list to store profit/loss changes
    profitLoss = []
    # Initialize first row value
    before = 0
    # Initialize change amount
    changeAmount = 0

    # Initialize max variables
    maxIncreaseAmount = 0
    maxIncDate = ""
    maxDecreaseAmount = 0
    maxDecDate = ""

    # Read through each row of data after the header
    for row in csvreader:
        monthCount += 1
        netTotal += int(row[1])
        changeAmount = int(row[1])-int(before)
        profitLoss.append(int(row[1]))
        if changeAmount > int(maxIncreaseAmount):
            maxIncDate = row[0]
            maxIncreaseAmount = changeAmount
        if changeAmount < int(maxDecreaseAmount):
            maxDecDate = row[0]
            maxDecreaseAmount = changeAmount
        before = row[1]

    # Find average of the changes in profit/loss
    indexLastProfit = len(profitLoss)-1
    sumChanges = profitLoss[indexLastProfit]-profitLoss[0]
    averageChange = sumChanges/indexLastProfit
    averageRounded = round(averageChange,2)

    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {monthCount}")
    print(f"Total: ${netTotal}")
    print(f"Average Change: ${averageRounded}")
    print(f"Greatest Increase in Profits: {maxIncDate} (${maxIncreaseAmount})")
    print(f"Greatest Decrease in Profits: {maxDecDate} (${maxDecreaseAmount})")

