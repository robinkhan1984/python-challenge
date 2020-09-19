import os
import csv

electiondata = os.path.join("Resources", "election_data.csv")
votes = 0 
voterid = []
candidate = []
numberofvotes = {}

# The total number of votes cast

with open(electiondata, 'r') as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")
    header = next(csvreader)
    for row in csvreader:
        voterid.append(row[0])
        

 
        
        politician = row[2]
        if politician not in candidate:
            candidate.append(politician)
        if politician not in numberofvotes:
            numberofvotes[politician] = 1
        else:
            numberofvotes[politician] = numberofvotes[politician] + 1


countofvotes = len(voterid)
winner = max(numberofvotes.values())
for name, value in numberofvotes.items():   
    if value == winner: 
        show_name = name
        

percent = ''
for x in candidate:
    percent += f"{x}: {numberofvotes[x]/((countofvotes))*100:.2f}%\n"

file = os.path.join("Analysis","PyPoll_Results.txt")

mult = ''' print '''
output = (f'''
Election Results
-------------------------
Total Votes: {countofvotes}
-------------------------
{politician}: {percent}-------------------------
Winner: {show_name}
-------------------------

''')

print(output)

with open(file, 'w') as text:
    text.writelines(output
)
  















