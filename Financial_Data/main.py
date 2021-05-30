import os
import csv

#Path to collect data from the Resource folder and print a text file to export
budget_data = os.path.join('Resources', 'budget_data.csv')
Analysis_PyBank = os.path.join('Analysis', 'Results_PyBank.txt')

# The total number of months of profits and losses
# The average changes in Profit/Losses over the entire period
# The Greatest increase in profits (date and amount) over the entire period
# The Greatest decrease in profits (date and amount) over the entire period
# The Greatest decrease in losses (date and amount) over the entire period

file = open(Analysis_PyBank, 'w')

Total_months = 0
Net_total = 0

index = 0
previous_profit = 0
Total_change = 0
Max_change = -99999999
Min_change = 99999999

with open(budget_data, 'r') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first if present
    csv_header = next(csvreader)

    for row in csvreader:
        Total_months = Total_months + 1
        Current_profit = int(row[1]) 
        Net_total = Net_total + Current_profit
        if index != 0:
            Current_change = Current_profit - previous_profit
            if Current_change > Max_change:
                Max_change = Current_change
            if Current_change < Min_change:
                Min_change = Current_change
        else:
            Current_change = 0
        previous_profit = Current_profit
        Total_change += Current_change
        index += 1
    
    Average_change = Total_change/(index + 1)

    # look into using a variable to print instead of multiple print statements
    print (f"Total number of months:{(Total_months)}")
    print (f"Net total amount of Profit/losses: {int(Net_total)}")
    print (f"The average in the changes in Profit/losses: {(Average_change)}")
    print (f"The greatest increase in Profits: {int(Max_change)}")
    print (f"The greatest decrease in Profits: {int(Min_change)}")
    
    file.write("Total number of months: {}\n".format(Total_months))
    file.write("Net total amount of Profit/losses: {}\n".format(int(Net_total)))
    file.write("The average in the changes in Profit/losses: {:0.2f}\n".format(Average_change))
    file.write("The greatest increase in Profits: {}\n".format(int(Max_change)))
    file.write("The greatest decrease in Profits: {}\n".format(int(Min_change)))


file.close()