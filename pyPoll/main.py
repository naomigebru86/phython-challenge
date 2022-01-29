import csv 
file = open("pyPoll/election_data.csv")
csv_file=csv.reader(file)
header=[]
rows=[]
for row in csv_file:
    rows.append(row)

candidate_name =[]
for i in rows:
    candidate_name.append(i[2])
dict_n={"Khan":0,"Correy":0,"Li":0, "O'Tooley":0}
for i in range(1,len(candidate_name)): 
    dict_n[candidate_name[i]]+=1
Khan_average=(dict_n["Khan"]/(len(rows)-1))*100
Li_average=(dict_n["Li"]/(len(rows)-1))*100
Correy_average=(dict_n["Correy"]/(len(rows)-1))*100
print(f"Election Votes")
print(f"--------------------------")
print(f"total votes={len(rows)-1}")
print(f"---------------------------")
print(dict_n)
print(f"Khan average= {Khan_average}")
print(f"Li average= {Li_average}")
print(f"Correy average= {Correy_average}")
print(f"---------------------------")
print(f"Winner: Khan")
print(f"---------------------------")

