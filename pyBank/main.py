import csv
file = open('pyBank/budget_data.csv')
csvfile = csv.reader(file)
header =[]
rows=[]
for row in csvfile:
    rows.append(row)
total=0

for v in rows:
    if v[1].isdigit():
      total=total+int(v[1])

profit_loss = []
for i in rows:
    if i[1].isdigit():
        profit_loss.append(i[1])

average_change=[]
for x in range(len(profit_loss)-1):
    average_change.append(int(profit_loss[x+1])-int(profit_loss[x]))
print(average_change)

avg_average_change =0
total_avg_change = 0
for i in average_change:
    avg_average_change+=i
total_avg_change = avg_average_change/len(average_change)

greatest_increase= max(average_change)
greatest_decrease= min(average_change)


print("financial analysis")
print("--------------------------")
print(f"total months: {len(rows)-1}")
print(f"total {total}")
print(f"Total average change : {total_avg_change}")
print(f"Greatest increase ={greatest_increase}")
print(f"Greatest decrease = {greatest_decrease}")
 
text_financial_analysis =open("analysis/financial analysis","a")
text_financial_analysis.write("financial analysis")
text_financial_analysis.write("\n--------------------------")
text_financial_analysis.write((f"\ntotal months: {len(rows)-1}"))
text_financial_analysis.write(f"\ntotal {total}")
text_financial_analysis.write(f"\nTotal average change : {total_avg_change}")
text_financial_analysis.write(f"\nGreatest increase ={greatest_increase}")
text_financial_analysis.write(f"\nGreatest decrease = {greatest_decrease}")


