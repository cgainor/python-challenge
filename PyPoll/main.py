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
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read the header row first
    csv_header = next(csvfile)

    # Initialize counting variable
    totalVoteCount = 0

    # Initialize candidate name dictionary
    candidateDict = {}

    # Read through each row of data after the header
    for row in csvreader:
        totalVoteCount += 1
        if row[2] in candidateDict:
            candidateDict[row[2]] += 1
        else:
            candidateDict[row[2]] = 1


    # Print analysis to terminal
    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: {totalVoteCount}")
    print("-------------------------")

    # Export a text file with the results
    newFile = open("PyPollResults.txt", "w")
    newFile.write("Election Results\n")
    newFile.write("-------------------------\n")
    newFile.write(f"Total Votes: {totalVoteCount}\n")
    newFile.write("-------------------------\n")

    # Initialize Winner variable
    winningAmount = 0
    winningName = ""

    # Loop through candidate dictionary and print out data to terminal and results text file
    for key in candidateDict:
        candidateName = key
        candidatePercentVotes = round((candidateDict[key]/totalVoteCount)*100, 3)
        candidateVoteCount = candidateDict[key]

        if candidateVoteCount > winningAmount:
            winningAmount = candidateVoteCount
            winningName = candidateName

        print(f"{candidateName}: {candidatePercentVotes}% ({candidateVoteCount})")
        newFile.write(f"{candidateName}: {candidatePercentVotes}% ({candidateVoteCount})\n")
    
    print("-------------------------")
    newFile.write("-------------------------\n")
    
    # Print winner name and write it to results text file
    print(f"Winner: {winningName}")
    print("-------------------------")
    newFile.write(f"Winner: {winningName}\n")
    newFile.write("-------------------------\n")

    # Close text file
    newFile.close()