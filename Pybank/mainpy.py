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
import statistics

# Set path for file
csvpath = os.path.join("..", "resources", "budget_data.csv")

greatest_increase =0
greatest_decrease =0
increase_month =[]
decrease_month =[]
months =[]
profit =[]
monthly_diff =[0]
changes_totaled =0
total_changes =0
average_change =0

# Open the CSV
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

    #list values for months and profit
    #calculate total profit
    total_profit=0
    for row in csvreader:
        total_profit += int(row[1])
        months.append(row[0])
        profit.append(row[1])
        # remove this and total profit fails....
        monthly_diff= profit
         
    # Calculate total Months
    months_total = len(months)

    profit = [int (i) for i in profit]
    # Calculate price changes, store values as monthly_diff
    for i in range(0, months_total-1):
        monthly_diff[i] = int(profit[i+1]-profit[i])
    monthly_diff.append(int(profit[i+1]-profit[i]))
    k=2
    res=monthly_diff[: -k or None]

    # Capture values (increase, decrease, dates, and average)
    greatest_increase = max(profit)
    greatest_decrease = min(profit)
    changes_totaled = sum(res)
    total_changes = len(res)
    MaxDateSpot=profit.index(greatest_increase)
    MinDateSpot=profit.index(greatest_decrease)
    increase_month=months[MaxDateSpot]
    decrease_month=months[MinDateSpot]
    average_change = (changes_totaled/total_changes)

    # print results
    print (f'Financial Analysis: \n  Total Months: {months_total} \
        \n  Total Profit: ${total_profit} \n  Average Change: ${average_change} \
        \n  Greatest Increase in Profits: {increase_month} (${greatest_increase}) \
        \n  Greatest Decrease in Profits: {decrease_month} (${greatest_decrease})')

# set output path and file name.
output = os.path.join("..", "analysis", "budget_analysis.csv")
with open(output, 'w') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    # create lists
    lables=['Label', 'total months', 'total profit', 'average change', 'greatest increase month', 'greatest increase', 'greatest decrease month', 'greatest decrease', ]
    data=['Data', months_total, total_profit, average_change, increase_month, greatest_increase, decrease_month, greatest_decrease]
    # convert list to rows and write to .csv
    rows=zip(lables, data)
    for row in rows:
        csvwriter.writerow(row)

    # # print (res)
    # # print (profit)
    # # print (total_changes)
    # # calculate average change
    # # average_change = sum(int(monthly_diff))
    # print (greatest_increase)
    # print (greatest_decrease)
    # print (average_change)
    # print (increase_month)
    # print (decrease_month)
    # # print (monthly_diff[i])
    # print (total_profit)
    # # print (months_total)
    # # print (greatest_increase)
    # # print (greatest_decrease)