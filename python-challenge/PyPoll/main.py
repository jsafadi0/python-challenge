import os
import csv
path_to = os.path.join(".", "Resources", "election_data.csv")
with open(path_to, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    candidate_list = [candidate[2] for candidate in csvreader]
total_votes = len(candidate_list)
candidate_info = [[candidate, candidate_list.count(candidate)] for candidate in set(candidate_list)]
candidate_info = sorted(candidate_info, key=lambda x: x[1], reverse=True)


print("Election Results")
print("-"*28)
print(f"Total Votes: {total_votes}")
print("-"*28)
for candidate in candidate_info:
    votes_percentage = (candidate[1] / total_votes) * 100
    print(f"{candidate[0]}: {votes_percentage:6.3f}% ({candidate[1]})")
print("-"*28)
print(f"Winner: {candidate_info[0][0]}")
print("-"*28)

path_to = os.path.join(".", "analysis", "Results.txt")
with open(path_to, "w") as text_file:
    print("Election Results", file=text_file)
    print("-"*28, file=text_file)
    print(f"Total Votes: {total_votes}", file=text_file)
    print("-"*28, file=text_file)
    for candidate in candidate_info:
        votes_percentage = (candidate[1] / total_votes) * 100
        print(f"{candidate[0]}: {votes_percentage:6.3f}% ({candidate[1]})", file=text_file)
    print("-"*28, file=text_file)
    print(f"Winner: {candidate_info[0][0]}", file=text_file)
    print("-"*28, file=text_file)