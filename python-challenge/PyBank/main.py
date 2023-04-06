import os
import csv
path_to = os.path.join(".", "Resources", "budget_data.csv")
total_month = []
total_amount = []
change = []

with open(path_to, newline="") as budget:
    csvreader = csv.reader(budget,delimiter=",")
    header = next(csvreader)
    for row in csvreader:
        total_month.append(row[0])
        total_amount.append(int(row[1]))
    
    for a in range(len(total_amount)-1):
        change.append(total_amount[a+1]-total_amount[a])

greatest_increase = max(change)
greatest_decrease = min(change)

monthly_increase = change.index(max(change)) + 1
monthly_decrease = change.index(min(change)) + 1


print("Financial Analysis")
print("-"*28)
print(f"Total Months: {len(total_month)}")
print(f"Total: ${sum(total_amount)}")
print(f"Average Change: ${round(sum(change)/len(change),2)}")
print(f"Greatest Increase in Profits: {total_month[monthly_increase]} (${(str(greatest_increase))})")
print(f"Greatest Decrease in Profits: {total_month[monthly_decrease]} (${(str(greatest_decrease))})")

path_to = os.path.join(".", "analysis", "Results.txt")
with open(path_to, "w") as text_file:
    print("Financial Analysis", file=text_file)
    print("-"*28, file=text_file)
    print(f"Total Months: {len(total_month)}", file=text_file)
    print(f"Total: ${sum(total_amount)}", file=text_file)
    print(f"Average Change: ${round(sum(change)/len(change), 2)}", file=text_file)
    print(f"Greatest Increase in Profits: {total_month[monthly_increase]} (${(str(greatest_increase))})", file=text_file)
    print(f"Greatest Decrease in Profits: {total_month[monthly_decrease]} (${(str(greatest_decrease))})", file=text_file)




    
