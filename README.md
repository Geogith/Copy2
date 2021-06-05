# Using Python for "Big Data" Analysis

# SUMMARY

Two large datasets were used to showcase the limits of an Excel-based analysis (Crowdfunding and Stock Market Projects) compared to using Python. Two robust Python scripts were written in Visual Studio Code (VSCode). Each script runs separately to make sure the code works for its respective dataset: Financial data and Voting data. The two datasets are uniquely different. One dataset if from a bank and the other is voting data from a rural town. Each dataset requires a thoughtful break down of tasks into discrete mini-objectives to render the printing of the analysis to the terminal for immediate visual results and exporting a text file of the results for documentation purposes.

 # FINANCIAL DATA SET - PORTION OF PYTHON CODE:

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
    

 # VOTING DATA SET - PORTION OF PYTHON CODE:
 
    print (f"Total number of votes:{(Total_vote)}")
    print (f"All the candidates:{list(Candidate.keys())}") 
    file.write(f"Total number of votes:{(Total_vote)}\n")
    file.write(f"All the candidates:{list(Candidate.keys())}\n")
    
    for k, v in Candidate.items():
        print ('Candidate {} got {} votes which is {:.2f}% of total votes'.format(k, v, v * 100.0 / Total_vote))     
        file.write('Candidate {} got {} votes which is {:.2f}% of total votes\n'.format(k, v, v * 100.0 / Total_vote))
        
        if v > winner_vote_count:
            winner_vote_count = v
            winner = k
    print (f"The winner is: {(winner)}")
    file.write (f"The winner is: {(winner)}\n")

file.close()

Total number of votes:3521001
All the candidates:['Khan', 'Correy', 'Li', "O'Tooley"]
Candidate Khan got 2218231 votes which is 63.00% of total votes
Candidate Correy got 704200 votes which is 20.00% of total votes
Candidate Li got 492940 votes which is 14.00% of total votes
Candidate O'Tooley got 105630 votes which is 3.00% of total votes
The winner is: Khan

