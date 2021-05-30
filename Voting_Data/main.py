import os
import csv

#Path to collect data from the Resource folder
election_data = os.path.join('Resources', 'election_data.csv')
Analysis_PyPoll = os.path.join('Analysis', 'Results_PyPoll.txt')


file = open(Analysis_PyPoll, 'w')

Total_vote = 0
Candidate = {}
winner = ''
winner_vote_count = -999999999

with open(election_data, 'r') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first if present
    csv_header = next(csvreader)

    for row in csvreader:
        Total_vote = Total_vote + 1
        Candidate_name = row[2]
        if Candidate_name not in Candidate:
        	Candidate[Candidate_name] = 0
        Candidate[Candidate_name] += 1
        
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
  