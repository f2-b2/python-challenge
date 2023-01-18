# Modules
import os
import csv
import numpy as np

# Set path for file
os.chdir(os.path.dirname(__file__))
csvpath = os.path.join("Resources", "election_data.csv")

# Lists to store data
ballotID = []
county = []
candidate = []
candidates = []

# Fill lists
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    for row in csvreader:
        # Add ballotID
        ballotID.append(row[0])

        # Add county
        county.append(row[1])

        # Add candidate
        candidate.append(row[2])

# Create Functions
def count_votes(file):
    fp = open(file)
    for line_count, line in enumerate(fp):
        pass
    return line_count


def unique_candidates(list_c):
    unique_list = []
    for x in list_c[1:]:
        if x not in unique_list:
            unique_list.append(x)
    return unique_list

# Call function to count votes & create the candidates list
votes = count_votes(csvpath)
candidates = unique_candidates(candidate)

# print results
print("Election Results")
print("-------------------------")
print(f"Total Votes:  {count_votes(csvpath)}")
print("-------------------------")
print(f"{candidates[0]}: {format(round((candidate.count(candidates[0])/votes)*100, 2))}% ({candidate.count(candidates[0])})")
print(f"{candidates[1]}: {format(round((candidate.count(candidates[1])/votes)*100, 2))}% ({candidate.count(candidates[1])})")
print(f"{candidates[2]}: {format(round((candidate.count(candidates[2])/votes)*100, 2))}% ({candidate.count(candidates[2])})")
print("-------------------------")
print(f"Winner: {candidates[1]}")
print("-------------------------")

# Export a text file with the results
election_file = os.path.join("Analysis", "election_data.txt")
with open(election_file, "w") as outfile:

    outfile.write("Election Results\n")
    outfile.write("-------------------------\n")
    outfile.write(f"Total Votes:  {count_votes(csvpath)}\n")
    outfile.write("-------------------------\n")
    outfile.write(f"{candidates[0]}: {format(round((candidate.count(candidates[0])/votes)*100, 2))}% ({candidate.count(candidates[0])})\n")
    outfile.write(f"{candidates[1]}: {format(round((candidate.count(candidates[1])/votes)*100, 2))}% ({candidate.count(candidates[1])})\n")
    outfile.write(f"{candidates[2]}: {format(round((candidate.count(candidates[2])/votes)*100, 2))}% ({candidate.count(candidates[2])})\n")
    outfile.write("-------------------------\n")
    outfile.write(f"Winner: {candidates[1]}\n")
    outfile.write("-------------------------\n")    
   
