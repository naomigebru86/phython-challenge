# import the csv file
import csv 
file = open("pyPoll/election_data.csv")

# register the csv file to csv_file variable
csv_file=csv.reader(file)
header=[]
rows=[]

# create a nested list of rows 
for row in csv_file:
    rows.append(row)

# get total votes
total = len(rows)-1

#append candiate names to a list 
candidate_name =[]
for i in range(0,len(rows)):
    candidate_name.append(rows[i][2])

# create a dictionary of candidates
dict_n={}
for i in range(1,len(candidate_name)):
    if candidate_name[i] in dict_n.keys():
        dict_n[candidate_name[i]]+=1
    else:
         dict_n[candidate_name[i]]=1
print(dict_n)

# dictionary of candidates with thier number of votes and percente
dict_candidates={}
for k,v in dict_n.items():
    dict_candidates[k]=[round((v/total)*100,2),v]
print(dict_candidates)

#get the winner
winner =""
max= 0
for k,v in dict_candidates.items():
    if v[1]>max:
        max=v[1]
        winner=k

#print the output to console
print(f"Election Votes")
print(f"--------------------------")
print(f"total votes={total}")
print(f"---------------------------")
for k,v in dict_candidates.items():
    print(f"{k}: {v[0]}% ({v[1]})")
print(f"---------------------------")
print(f"Winner: {winner}")
print(f"---------------------------")

# save the output to text file
text_election_analysis = open("analysis/Election Results","a")
text_election_analysis.write("Election Results")
text_election_analysis.write(f"\n-------------------------")
text_election_analysis.write(f"\nTotal Votes: {total}")
text_election_analysis.write(f"\n-------------------------")
for k,v in dict_candidates.items():
    text_election_analysis.write(f"\n{k}: {v[0]}% ({v[1]})")
text_election_analysis.write(f"\n-------------------------")
text_election_analysis.write(f"\nWinner: {winner}")
text_election_analysis.write(f"\n-------------------------")
