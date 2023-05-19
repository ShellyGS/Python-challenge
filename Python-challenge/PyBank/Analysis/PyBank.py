#!/usr/bin/env python
# coding: utf-8

# In[12]:


#To create file paths across operating systems
import csv
import os

# To read the CSV file
Py_bank_csv = os.path.join('..',Resources','budget_data.csv')

# Initialize variables
Total_months = 0
Net_total = 0
Previous_profit = 0
Change = []
Greatest_increase = ['', 0]
Greatest_decrease = ['', 0]

# Read the CSV file
with open(Py_bank_csv, 'r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)  # To skip the header row

    # Iterate through each row in the CSV file
    for row in csv_reader:
        # Update the total number of months
        Total_months = Total_months + 1

        # Extract the profit/loss value from the row
        Profit = int(row[1])

        # Calculate the net total profit/loss
        Net_total = Net_total + Profit

        # Calculate the change in profit/loss from the previous row
        if Total_months > 1:
            Difference = Profit - Previous_profit
            Change.append(Difference)

            # Check for the greatest increase in profits
            if Difference > Greatest_increase[1]:
                Greatest_increase = [row[0], Difference]

            # Check for the greatest decrease in profits
            if Difference < Greatest_decrease[1]:
                Greatest_decrease = [row[0], Difference]

        # Update the previous profit/loss value
        Previous_profit = Profit

# Calculate the average change in profit/loss
average_change = sum(Change) / len(Change)

# Print the analysis results
print("--------------------")
print("Financial Analysis")
print("--------------------")
print(f"Total Months: {Total_months}")
print(f"Total: ${Net_total}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {Greatest_increase[0]} (${Greatest_increase[1]})")
print(f"Greatest Decrease in Profits: {Greatest_decrease[0]} (${Greatest_decrease[1]})")


# Export the analysis results to a text file
output_file = "Budget_analysis.txt"
with open(output_file, "w") as file:
    file.write("-----------------------\n")
    file.write("Financial Analysis\n")
    file.write("-----------------------\n")
    file.write("Total Months: " + str(Total_months) + "\n")
    file.write("Net Total: $" + str(Net_total) + "\n")
    file.write("Average Change: $" + "{:.2f}".format(average_change) + "\n")
    file.write("Greatest Increase in Profits: " + Greatest_increase[0] + " ($" + str(Greatest_increase[1]) + ")\n")
    file.write("Greatest Decrease in Profits: " + Greatest_decrease[0] + " ($" + str(Greatest_decrease[1]) + ")\n")


# In[ ]:





# In[ ]:




