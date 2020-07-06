# Your task is to create a Python script that analyzes the records to calculate each of the following:

    # The total number of months included in the dataset
    # The net total amount of "Profit/Losses" over the entire period
    # The average of the changes in "Profit/Losses" over the entire period
    # The greatest increase in profits (date and amount) over the entire period
    # The greatest decrease in losses (date and amount) over the entire period

# As an example, your analysis should look similar to the one below:
    # Financial Analysis
        # Total Months: 86
        # Total: $38382578
        # Average  Change: $-2315.12
        # Greatest Increase in Profits: Feb-2012 ($1926159)
        # Greatest Decrease in Profits: Sep-2013 ($-2196167)

# In addition, your final script should both print the analysis to the terminal and export a text file with the results.

# Modules
import os
import csv

# Set path for file
csvpath = os.path.join("Resources", "budget_data.csv")
# output = os.path.join("Analysis", "budget_analysis.csv")

monthly_change =[]
Profit_Loss = []
profit_change =0
greatest_decrease = 0
greatest_increase = 0
profit_total = 0

# Open the CSV
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile)

    csv_header = next(csvreader)
    
    for row in csvreader:
        # date = row[0]
        profit_total += int(row[1])
        monthly_total = len(list(csvreader))+1
        average = profit_total/monthly_total
        #if int(row[1])-next(int(row[1])) > then greatest 
        # then greatest_increase = int(row[1])-next(int(row[1]))
        # greatest_increase_month = row[0]
        print (profit_total)
        
    # Profit_loss=[int(i) for i in PL]
    # for i in range(0, len(PL)-1):
    #     profit_change[i]=PL[i+1]-PL[i]
    #     profit_change.append(PL[i+1]-PL[i])
    #     greatest_increase =  max(profit_change)
    #     greatest_decrease = min(profit_change)


        # zip month to greatest increse and decrease for output
        # avg = profit - profit(row+1)/mt
        # append the list to create a new “colum” for the next month then do the subtraction.
        # for i in range(1, len(list)) #subtract next row from this row.  
    # MP = max [1]
    # Gl = min [1]



