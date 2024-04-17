import os
import csv


#Placing Input and Output
Poll_Data = os.path.join('Resources/', "election_data.csv")
Poll_Results_Output = os.path.join("Analysis", "Poll_Results_Output.txt")


total_vote = 0
candidates_list = []

#Use a dictionary to store canditates and their votes
vote_counts = {}
vote_ratio = {}

#Open and Read in CSV File
with open(Poll_Data) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ",")

    #Skip Header Row
    csv_header = next(csv_reader)

    #First loop through totals to find candidates
    for row in csv_reader:

        total_vote += 1
        candidate_name = row[2]

        #Using if statement to list candidates with certain values
        if row[2] not in candidates_list:
            candidates_list.append(row[2])
            vote_counts[candidate_name] =0
        #Calculates total vote per candidate
        vote_counts[candidate_name] += 1

#Calcuates the percentage of votes per candidate
for i in vote_counts:
    vote_ratio[i]= (vote_counts[i]/total_vote)

#Finds the Winner of the election
inverse = [(value,key) for key,value in vote_counts.items()]
Winner = max(inverse)[1]

#Variables for Results
First_Candidate = list(vote_counts.keys())[0]
Second_Candidate = list(vote_counts.keys())[1]
Third_Candidate = list(vote_counts.keys())[2]

First_Candidate_votes = list(vote_counts.values())[0]
Second_Candidate_votes = list(vote_counts.values())[1]
Third_Candidate_votes = list(vote_counts.values())[2]


First_Percent = (list(vote_ratio.values())[0]) * 100
Second_Percent = (list(vote_ratio.values())[1]) * 100
Third_Percent = (list(vote_ratio.values())[2]) * 100




#Save Output to Print Text File
Output = (
"Election Results\n"
"--------------------\n"
f"Total Votes: {total_vote}\n"
"----------------------\n"
f"{First_Candidate} : {First_Percent:.3f}% ({First_Candidate_votes})\n"
f"{Second_Candidate} : {Second_Percent:.3f}% ({Second_Candidate_votes})\n"
f"{Third_Candidate} : {Third_Percent:.3f}% ({Third_Candidate_votes})\n"
"-----------------------\n"
f"Winner: {Winner}")

#Print Election Results
print(Output)

#Export to Text File
with open(Poll_Results_Output, "w") as txt_file:
    txt_file.write(Output)
