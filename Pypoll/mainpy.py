#in this challenge, you are tasked with helping a small, rural town modernize its vote counting process.

# You will be give a set of poll data called election_data.csv. The dataset is composed of three columns: 
# Voter ID, County, and Candidate. Your task is to create a Python script that analyzes the votes and 
# calculates each of the following:

# The total number of votes cast
# A complete list of candidates who received votes
# The percentage of votes each candidate won
# The total number of votes each candidate won
# The winner of the election based on popular vote.

# As an example, your analysis should look similar to the one below:
#     Election Results
#         -------------------------
#         Total Votes: 3521001
#         -------------------------
#         Khan: 63.000% (2218231)
#         Correy: 20.000% (704200)
#         Li: 14.000% (492940)
#         O'Tooley: 3.000% (105630)
#         -------------------------
#         Winner: Khan
#         -------------------------

# In addition, your final script should both print the analysis to the terminal and export a text file with the results.

# Modules
import os
import csv

# Set path for file
csvpath = os.path.join("Resources", "election_data.csv")

candidates = []
votes =0
total_votes =0
# County = []
# percent = 0

# Open the CSV
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)

    for row in csvreader:
        candidate = row[2]
        votes = row[0]
        # total_votes = len(row[0])
        if candidate not in candidates:
            candidates.append(candidate)
       
        #     vote_tally[candidate]+=1
        # if candidate in candidates:
        #     vote_tally[candidate]+=1
    # vote_tally[candidate]-0
    # vote_tally[candidate]+=1
    # iterate over list of unique candidates
    # for candidate in candidates:
    #     vote_tally[candidate] = [0,0]
    # percent = vote_tally/total_votes

print (candidates)
# print (vote_tally)
# print (total_votes)
    
# winner = max(candidate_votes)

# output = os.path.join("Analysis", "election_results")
# with open(output, 'w') as csvfile:
# csvwriter = csv.writer(csvfile, delimiter=",")#
