#Import the budget_data.csv file
import csv
file = open('pyBank/budget_data.csv')
# csvfile variable that represents the csv file
csvfile = csv.reader(file)
header =[]
rows=[]
# append every row of csv file to the list "rows"
#it'll be a nested list of rows[[x,y]],where x is the Date and y is Profit/Losses
for row in csvfile:
    rows.append(row)
# total variable to register the net total of Profit/Losses
total=0
#iterate thru the rows list and add Profit/Losses to the total
# isdigit() is used because the first element on the list rows is [Date,Profit/Losses]
#isdigit() can be used incase of anomalies in the data, for example; if data type other than integer present in the Profit/Losses column
for v in rows:
    if v[1].isdigit():
      total=total+int(v[1])

# create profit_loss list to register the Profit/Losses column
profit_loss = []
for i in rows:
    if i[1].isdigit():
        profit_loss.append(i[1])

# average_change list to register the average change between consecutive dates
average_change=[]
for x in range(len(profit_loss)-1):
    average_change.append(int(profit_loss[x+1])-int(profit_loss[x]))

# find the average change over the period of time
avg_average_change =0
total_avg_change = 0
for i in average_change:
    avg_average_change+=i
total_avg_change = avg_average_change/len(average_change)

# find the greatest increase
greatest_increase= max(average_change)

# find the greatest decrease
greatest_decrease= min(average_change)


print("Financial Analysis")
print("--------------------------")
print(f"Total Months: {len(rows)-1}")
print(f"Total: ${total}")
print(f"Average change: ${round(total_avg_change,2)}")
print(f"Greatest Increase in Profits: ${greatest_increase}")
print(f"Greatest Decrease in Profits: ${greatest_decrease}")
 
#save the output to external text file text_financial_analysis
text_financial_analysis =open("analysis/financial analysis","a")
text_financial_analysis.write("Financial Analysis")
text_financial_analysis.write("\n--------------------------")
text_financial_analysis.write((f"\nTotal Months: {len(rows)-1}"))
text_financial_analysis.write(f"\nTotal: ${total}")
text_financial_analysis.write(f"\nAverage change: ${round(total_avg_change,2)}")
text_financial_analysis.write(f"\nGreatest Increase in Profits: ${greatest_increase}")
text_financial_analysis.write(f"\nGreatest Decrease in Profits: ${greatest_decrease}")


