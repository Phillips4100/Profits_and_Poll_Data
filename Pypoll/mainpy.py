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
csvpath = os.path.join("..", "Resources", "election_data.csv")

candidates = []
total_votes =0
candidate=[]
counter =0
vote_tally={}
winner =[]

# Open the CSV
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)
    
    #get count of total votes
    votes=[]
    for row in csvreader:
        counter = counter + 1
        votes.append(row[2])
           
# get a list of candidates
        candidate = row[2]
        if candidate not in candidates:
            candidates.append(candidate)

# build dictionary of unique candidates and calculate votes / percentages
    vote_tally ={}
    for candidate in candidates:
        vote_tally[candidate] = round(((list.count(votes, candidate))/(counter)*100),2), (list.count(votes, candidate))
    
    winner  = max(vote_tally, key=vote_tally.get)

print (f'Election Results: \n \
------------------------- \n \
Total Votes: {counter} \n \
------------------------- \n \
Candidate: ( % , Total Votes)')
for key in vote_tally:
    print(key, ' : ', vote_tally[key])
print (f'------------------------- \n \
Winner: {winner} \n \
-------------------------')

#write results to csv file
output = os.path.join("..", "analysis", "election_results.csv")
with open(output, 'w') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    w = csv.writer(csvfile)
    w.writerows(vote_tally.items())

