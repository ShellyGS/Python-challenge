
import csv
import os

# Set the path to the CSV file
Pypoll_csv = os.path.join('..','Resources','election_data.csv')

# Initialize variables to hold the analysis results
Total_votes = 0
Candidates = {}
Winner = ""

# Read the CSV file
with open(Pypoll_csv, "r") as file:
    csv_reader = csv.reader(file, delimiter=",")
    next(csv_reader) # Skip the header row

    # Loop through each row in the dataset
    for row in csv_reader:
        Total_votes = Total_votes + 1 # Update the total number of votes cast
        Candidate_name = row[2]  # Update the number of votes for the current candidate
        if Candidate_name not in Candidates:
            Candidates[Candidate_name] = 1 #setting the counter to 1 as per the candidate
        else:
            Candidates[Candidate_name] = Candidates[Candidate_name] + 1

    # Determine the winner of the election
    Max_votes = 0
    for Candidate in candidates:
        Votes = Candidates[Candidate]
        if Votes > Max_votes:
            Max_votes = Votes
            Winner = Candidate

# Print the analysis results to the terminal
print("Election Results")
print("-------------------------")
print("Total Votes: " + str(Total_votes))
print("-------------------------")
for Candidate in Candidates:
    Votes = Candidates[Candidate]
    Vote_percent = Votes / Total_votes * 100
    print(Candidate + ": " + "{:.3f}".format(Vote_percent) + "% (" + str(Votes) + ")")
print("-------------------------")
print("Winner: " + Winner)
print("-------------------------")

# Export the analysis results to a text file
output_file_path = "Election_results.txt"
with open(output_file_path, "w") as file:
    file.write("Election Results\n")
    file.write("-------------------------\n")
    file.write("Total Votes: " + str(Total_votes) + "\n")
    file.write("-------------------------\n")
    for Candidate in Candidates:
        Votes = Candidates[Candidate]
        Vote_percent = Votes / Total_votes * 100
        file.write(Candidate + ": " + "{:.3f}".format(Vote_percent) + "% (" + str(Votes) + ")\n")
    file.write("-------------------------\n")
    file.write("Winner: " + Winner + "\n")

