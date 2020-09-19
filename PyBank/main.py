import os
import csv

budgetdata = os.path.join("Resources", "budget_data.csv")
months = 0
date = []
profitloss = []
difflist = []
revenue = 0

with open(budgetdata, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    for row in csvreader:
        date.append(row[0])
        profitloss.append(int(row[1]))

# The total number of months included in the dataset

    #    
# # The net total amount of "Profit/Losses" over the entire period
    for x in range(1,len(profitloss)):
        diff = profitloss[x] - profitloss[x-1]
        difflist.append(diff)


# # The average of the changes in "Profit/Losses" over the entire period
    sumofdiff = sum(difflist)
    lengthofdifflist = len(difflist)
    averagechange = sumofdiff/lengthofdifflist
    ageragechangerounded = round(averagechange,2)


# The greatest increase in profits (date and amount) over the entire period
maxincrease = max(difflist)
indexofmaxincrease = difflist.index(maxincrease)
maxdecrease = min(difflist)
indexofmaxdecrease = difflist.index(maxdecrease)

months = len(date) 
revenue = sum(profitloss)
# The greatest decrease in losses (date and amount) over the entire period



# file = os.path.join("Analysis/PyBank_Results.txt")

# with open(file, 'w') as text:
#     text.write(

mult = ''' print '''
print(f'''
Financial Analysis
----------------------------
Total Months: {months}
Total: ${revenue}
Average  Change: ${ageragechangerounded}
Greatest Increase in Profits: {date[indexofmaxincrease+1]} {maxincrease}
Greatest Decrease in Profits: {date[indexofmaxdecrease+1]} {maxdecrease}
''')



# file = os.path.join("Analysis/PyBank_Results.txt")

# with open(file, 'w') as text:
#     text.write(
#         print('Financial Analysis'),
#         print('----------------------------'),
#         print(f"Total Months: {months}"),
#         print(f"Total: ${revenue}"),
#         print(f"Average  Change: ${ageragechangerounded}"),
#         print(f"Greatest Increase in Profits: {date[indexofmaxincrease+1]} {maxincrease}"),
#         print(f"Greatest Decrease in Profits: {date[indexofmaxdecrease+1]} {maxdecrease}"),

# )
#     text.close

