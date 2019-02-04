## INSTRUCTIONS ##
# Given a set of poll data called election_data.csv
# 3 columns: "Voter ID", "County", and "Candidate"
# Create a python script that analyzes the votes and calculates:
        # The total number of votes cast
        # A complete list of candidates who received votes
        # The percentage of votes each candidate won
        # The total number of votes each candidate won
        # The winner of the election based on popular vote
    # Print analysis to terminal and export a text file with the results
# ---------------------------------------------------------------------------------

# Modules
import os
import csv

pyPoll_csv = os.path.join("Resources", "election_data.csv")

# Open and read csv
with open(pyPoll_csv, newline="") as csvfile:
    csvreader