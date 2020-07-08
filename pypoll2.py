# Modules
import os
import csv
from collections import Counter

# Set path for file
csvpath = os.path.join("Resources", "election_data.csv")

candidates = []
total_votes =0
candidate=[]
counter =0
vote_tally={}
# County = []
# percent = 0

# Open the CSV

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    header = next(csvreader)
    for row in csvreader:
        counter = counter + 1
           
# get a list of candidates
        candidate = row[2]
        if candidate not in candidates:
            candidates.append(candidate)

# build dictionary of unique candidates
    vote_tally ={}
    for candidate in candidates:
        vote_tally[candidate] = [0,0]

# total candidate votes
    for key, value in vote_tally.items():
        if key == row[2]:
            value[1] = value[1] + 1
            # percent votes for candidate
            value[0] = round(((value[1] / counter) * 100), 1)

# Identify winner   
    votes = 0         
    for key, value in vote_tally.items():
        if value[1] > votes:
            votes = value[1]
            # store corresponding candidate name
            winner = key

    # print (counter)
    # print (candidates)
    # print (vote_tally)
    # print (winner)

print (f'Election Results: \n \
    ------------------------- \n \
    Total Votes: {counter} \n \
    ------------------------- \n \
    {vote_tally} \n \
    ------------------------- \n \
    Winner: {winner} \n \
    -------------------------')
