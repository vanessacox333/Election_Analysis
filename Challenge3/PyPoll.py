# data we need to retrieve
# 1. Total number of votes cast
# 2. A complete list of candidates who recieved votes
# 3. The percentage of votes each candidate won
# 4. Total number of votes each candidate won
# 5. The winner of the election based on popular votes


# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")


# Initialize a total voter count
total_votes=0

# Candidate options
candidate_options=[]

# Candidate votes (empty dictionary)
candidate_votes={}

winning_candidate = ""
winning_count = 0 
winning_percentage = 0




# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data) 

    # Read the header row.
    headers = next(file_reader)

    # Print all rows 
    for row in file_reader:
        # Add to total voter count (every row = 1 vote)
        total_votes += 1 

        # Print candidates name for each row
        candidate_name=row[2]

        # If the candidates name has not been added to candidate options variable
        if candidate_name not in candidate_options:
            # Then add candidate name to candidate options variable
            candidate_options.append(candidate_name)

            # Begin tracking candidates votes
            candidate_votes[candidate_name]=0

        # Iterate through rows adding votes to each candidate
        candidate_votes[candidate_name] += 1


for candidate_name in candidate_votes:
    votes = candidate_votes[candidate_name]
    vote_percentage = float(votes) / float(total_votes) *100
    # Print vote percentage
    print(f"{candidate_name}: received {round(vote_percentage,1)} % of the vote.")

    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

    if votes > winning_count and vote_percentage > winning_percentage:
        winning_count = votes
        winning_percentage = vote_percentage
        winning_candidate = candidate_name

# Print total voter count
print(total_votes)

# Print candidate names
print(candidate_options)

# Print candidate votes
print(candidate_votes)

# Print winning count, %, and candidate
winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)


