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
print(len(voterid)) 
for x in candidate:
    print(x, numberofvotes[x], (numberofvotes[x]/(len(voterid)))*100)
                











# The total number of votes cast
print(len(voterid)) 

# for x in candidate
#     print

#     data = list(csvreader)
#     votes = len(data)
#     # votes = len(list(csvreader))
#     print("Election Results")
#     print("-------------------------")
#     print(f"Total Votes: {votes}")
#     print("-------------------------")

# #    A complete list of candidates who received votes
#     # sum = 0
#     # for row in data: 
#     #     Candidate = str(names[2])
#     #     Candidate = Candidate + 1
#     # print(Candidate)

#     dict = {}
#     for elem in data:
#         if elem[2] not in dict:
#           dict[elem[2]] = 0
#         dict[elem[2]] = dict[elem[2]] + 1
    
#     final_list = [{'num' : elem, 'count': dict[elem]} for elem in dict]
#     print(elem)



# #    The percentage of votes each candidate won





# #    The total number of votes each candidate won

# #    The winner of the election based on popular vote.














