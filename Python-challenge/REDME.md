# Module 3 Challenge

This challenge is about writing the python scripts for the real world situation tasks. The name of the challenges or tasks to be completed are “PyBank and “PyPoll”.

## Instructions:

### Preparation
1. Create new repository for this challenge
1. Clone the new repository to your computer.
1. Inside your local Git repository, create a folder for each Python assignment and name them PyBank and PyPoll.
1. Create two new folders Resources and analysis and main.py as script
### PyBank 
- The CSV file named “budget\_data.csv” is the financial dataset which is composed of two columns: "Date" and "Profit/Losses".
- The python script analysis the record to calculate mentioned below
  - The total number of months included in the dataset
  - The net total amount of "Profit/Losses" over the entire period
  - The changes in "Profit/Losses" over the entire period, and then the average of those changes
  - The greatest increase in profits (date and amount) over the entire period
  - The greatest decrease in profits (date and amount) over the entire period
- Steps:
  - Total months – this is counted using FOR loop and adding the total number of months as each row is visited
  - Net profit – loss – Extracting the profit/loss value in the row and adding the value in the previous value of the variable profit.
  - To calculates the difference in profits between tow months and append the difference to a list (Change), then check for the greatest increase and greatest decrease in profits while updating the corresponding variables, if a new record is found. Moreover assigning the value of the previous profit variable to profit variable.
  - The average change is calculated by summation of change divided by the length of change
  - Finally printing the analysis results using print ()
  - Also, export the analysis to a text file using file.write()
### PyPoll


- The CSV file named “election\_data.csv” is the poll dataset which is composed of three columns: "Voter ID", "County", and "Candidate"
- The python script analysis the record to calculate mentioned below
  - The total number of votes cast
  - A complete list of candidates who received votes
  - The percentage of votes each candidate won
  - The total number of votes each candidate won
  - The winner of the election based on popular vote
- Steps:
  - Total Votes – this is counted using FOR loop and adding the total number of votes as each row is visited
  - Candidate list– count the number of votes for each candidate and updating the counter to 1 if the candidate is new
  - To determine the winner, a variable is assigned as max\_votes, using FOR loop which counts the number of votes with the current candidate and assign it to variable vote.next step is to check the votes for current candidate is greater than the max number of votes.
  - Finally printing the analysis results using print ()
  - Also, export the analysis to a text file using file.write()	 

