# Import dependencies
import os
import csv

# Set path for file
csvpath = os.path.join(os.getcwd(), "Resources", "budget_data.csv")

#variables 
months_count = 0
net_total_profit_loss = 0
previous_profit_loss = 0
current_profit_loss = 0
profit_loss_delta = 0

#Lists to store data
months = []
changes = []

# Open and read csv
with open(csvpath, newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    
    # Store the header row
    header = next(csvfile)

    for row in csv_reader:
        # Count of months
        months_count += 1

        # Net total 
        current_profit_loss = int(row[1])
        net_total_profit_loss += current_profit_loss

        # For first month set previous month equal to current month 
        if (months_count == 1):
            previous_profit_loss = current_profit_loss
            
            # Continue skips adding to the lists for the first month
            continue 

        else:

            # Add each month to the months list
            months.append(row[0])

            # Calculate and add changes to changes list
            profit_loss_delta = current_profit_loss - previous_profit_loss
            changes.append(profit_loss_delta)

            # Set current_month_loss as previous_profit_loss 
            previous_profit_loss = current_profit_loss
            
            
#sum and average of the changes
sum_changes = sum(changes)
average_profit_loss = round(sum_changes/(months_count - 1), 2)

# max and min changes
max_change = max(changes)
min_change = min(changes)

# Locate the index value of max and min changes
max_change_index = changes.index(max_change)
min_change_index = changes.index(min_change)

# Assign best and worst month
best_month = months[max_change_index]
worst_month = months[min_change_index]

# -->>  Print the analysis to the terminal
print("Financial Analysis\n")
print("----------------------------\n")
print(f"Total Months:  {months_count}\n")
print(f"Total:  ${net_total_profit_loss}\n")
print(f"Average Change:  ${average_profit_loss}\n")
print(f"Greatest Increase in Profits:  {best_month} (${c})\n")
print(f"Greatest Decrease in Losses:  {worst_month} (${min_change})\n")


# -->>  Export a text file with the results
budget_file = os.path.join("Analysis", "budget_data.txt")
with open(budget_file, "w") as outfile:

    outfile.write("Financial Analysis\n")
    outfile.write("----------------------------\n")
    outfile.write(f"Total Months:  {months_count}\n")
    outfile.write(f"Total:  ${net_total_profit_loss}\n")
    outfile.write(f"Average Change:  ${average_profit_loss}\n")
    outfile.write(f"Greatest Increase in Profits:  {best_month} (${max_change})\n")
    outfile.write(f"Greatest Decrease in Losses:  {worst_month} (${min_change})\n")