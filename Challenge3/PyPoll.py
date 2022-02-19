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

# 1: Create a county list and county votes dictionary
county_list=[]
county_votes={}

winning_candidate = ""
winning_count = 0 
winning_percentage = 0

# 2: Track the largest county and county voter turnout.
largest_turnout=""
lt_votes = 0

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

        # 3: Extract the county name from each row.
        county_name=row[1]
    
        # If the candidates name has not been added to candidate options variable
        if candidate_name not in candidate_options:
            # Then add candidate name to candidate options variable
            candidate_options.append(candidate_name)

            # Begin tracking candidates votes
            candidate_votes[candidate_name]=0

        # Iterate through rows adding votes to each candidate
        candidate_votes[candidate_name] += 1

        # 4a: Write an if statement that checks that the county does not match any existing county in the county list.
        if county_name not in county_list:
            
            # 4b: Add the existing county to the list of counties.
            county_list.append(county_name)
            # 4c: Begin tracking the county's vote count.
            county_votes[county_name] = 0
        # 5: Add a vote to that county's vote count.
        county_votes[county_name] += 1



# Save the results to our text file.
with open(file_to_save, "w") as txt_file:

    # Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")

    # Save the final vote count to the text file.
    txt_file.write(election_results)



   # 6a: Write a for loop to get the county from the county dictionary.
    for county_name in county_votes:

        # 6b: Retrieve the county vote count.
        cvotes = county_votes[county_name]

        # 6c: Calculate the percentage of votes for the county.
        cvote_percentage = float(cvotes) / float(total_votes) *100

         # 6d: Print the county results to the terminal.
        county_results = (f"{county_name}: {cvote_percentage:.1f}% ({cvotes:,})\n")
        print(county_results)

         # 6e: Save the county votes to a text file.
        
        


         # 6f: Write an if statement to determine the winning county and get its vote count.
        
            
        


    # 7: Print the county with the largest turnout to the terminal.

    print(largest_turnout)

    # 8: Save the county with the largest turnout to a text file.
 


    for candidate_name in candidate_votes:
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes) / float(total_votes) *100
        # Print vote percentage
        print(f"{candidate_name}: received {round(vote_percentage,1)} % of the vote.")

        # Print each candidate, their voter count, and percentage to the terminal.
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        print(candidate_results)
        # Save the candidate results to our text file.
        txt_file.write(candidate_results)

        # print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

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
    # print(winning_candidate_summary)

    # Save the winning candidate's results to the text file.
    txt_file.write(winning_candidate_summary)


