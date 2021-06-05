# Using Python for "Big Data" Analysis

# SUMMARY

Two large datasets were used to showcase the limits of an Excel-based analysis (Crowdfunding and Stock Market Projects) compared to using Python. Two robust Python scripts were written in Visual Studio Code (VSCode). Each script runs separately to make sure the code works for its respective dataset: Financial data and Voting data. The two datasets are uniquely different. One dataset if from a bank and the other is voting data from a rural town. Each dataset requires a thoughtful break down of tasks into discrete mini-objectives to render the printing of the analysis to the terminal for immediate visual results and exporting a text file of the results for documentation purposes.

FINANCIAL DATA SET - PORTION OF PYTHON CODE:

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

    Total number of months: 86
    Net total amount of Profit/losses: 38382578
    The average in the changes in Profit/losses: -2261.90
    The greatest increase in Profits: 1926159
    The greatest decrease in Profits: -2196167
    
    _____________________________________________________________________________

VOTING DATA SET - PORTION OF PYTHON CODE:


