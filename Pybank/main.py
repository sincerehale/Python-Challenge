

import os
import csv

Data = os.path.join("Resources", "budget_data.csv")
Analysis_output = os.path.join("Analysis", "Analysis_output.txt")
Total_Months = 0
Total_Net = 0

#Open/Read the CSV File
with open(Data) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ",")

    #Skip Header
    csv_header = next(csv_reader)

    #Set list of difference in profits and losses
    Net_Change_list = []
    Month_Change_list = []

    #First loop through totals
    for row in csv_reader:
        #Calculate total months and total of profits/losses
        Total_Months += 1
        Total_Net += int(row[1])

        #Storing Net Change Values
        Net_Change = []
        Net_Change_list.append(int(row[1]))
        #Adding Month Change Values
        Month_Change_list.append(row[0])

        #Second loop for Calculations
        for i in range(1, len(Net_Change_list)):
            Net_Change.append(Net_Change_list[i]-(Net_Change_list[i-1]))


#Calculate Average Change
Average_Change = sum(Net_Change)/len(Net_Change)

#Greatest Profit/Loss in Net Change
Greatest_Profit = max(Net_Change)
Greatest_Loss = min(Net_Change)

#Find the month associted with Greatest Profit/Loss
index1 = Net_Change.index(Greatest_Profit)
index2 = Net_Change.index
