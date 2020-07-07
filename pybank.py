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
csvpath = os.path.join("resources", "budget_data.csv")
# output = os.path.join("Analysis", "budget_analysis.csv")

months_total = 0
profit_total = 0
average =0
Profit_Loss = []
greatest_decrease = 0
greatest_increase = 0
change = [0]
profit =0
months =[]
rows = 0

# Open the CSV
with open(csvpath) as csvfile:
	csvreader = csv.reader(csvfile, delimiter=',')
	header = next(csvreader)
	
	months_total = len(list(csvreader))
	
	print (header)

	for row in csvreader:
		print (row)
	
    # #identify values
		date = row[0]
		values =row[1]
		months.append(date)
		profit.append(values)
		profit_total += int(row[1])

    # calculate change in profit month to montn
	# profit = [int(i) for i in profit]
	# for i in range(0, len(profit)-1):
	# 	change[i] = profit[i]-profit[i+1]
	# 	change.append(profit[i]-profit[i+1])
		# profit_total.append(int(row[1]))
           
	# profit_total = sum(profit)
	# profit_total = sum(profit)
	average = profit_total/months_total   
	#calculate  min and max
	# greatest_increase = max(change)
	# greatest_decrease = min(change)

print (profit)
print (profit_total)
print (months)
# print (Date)
# print (months_total)    
# print (average)
# print (change)
# print (months)
        
    # Profit_loss=[int(i) for i in PL]
    # for i in range(0, len(PL)-1):
    #     profit_change[i]=PL[i+1]-PL[i]
    #     profit_change.append(PL[i+1]-PL[i])
    #     greatest_increase =  max(profit_change)
    #     greatest_decrease = min(profit_change)

# Print(f 'Financial Analysis \n Total: ${profit_total} \n Average Change: ${average_change} \n Greatest Monthly Increase: {increase_date} ${greatest_increase} \
#     \n Greatest Monthly Decrease: {decrease_date}${greatest_decrease}')




