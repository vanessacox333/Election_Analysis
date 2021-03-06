# School District Election Analysis
## Overview of Election Audit:
The purpose of this analysis is to assist the Colorado Board of Elections in an election audit for the United States Congressional Precinct in Colorado. The audit is typically done in Excel, but the Board of Elections wants to see how it can be done in Python, so that the code may be used across other congressional districts for election audits around the country.

## Election-Audit Results:
* There were 369,711 votes cast in this congressional election 
* Jefferson County had a total of 38,855 votes, representing 10.5% of the total vote
* Denver County had a total of 306,055 votes, representing 82.8% of the total vote
* Arapahoe County had a total of 24,801 votes, representing 6.7% of the total vote
* Denver County had the largest number of votes 
* Charles Casper Stockham had a total of 85,213 votes, representing 23.0% of the total candidate votes received
* Raymon Anthony Doane had a total of 11,606 votes, representing 3.1% of the total candidate votes received
* Diana DeGette was the winner of the election with a total of 272,892 votes, representing 73.8% of the total candidate votes received

## Election-Audit Summary: 
The code used to obtain the Colorado election results can be replicated among other congressional precinct elections so long as election data is stored in a .csv file with the same format as the Colorado election .csv file (Column 1: "Voter ID", Column 2: "County", Column 3: "Candidate"). If so, the only part of the script that will need to be edited is the code to load and save the .csv and .txt files:

import csv\
import os\
file_to_load = os.path.join("Resources", "election_results.csv")\
file_to_save = os.path.join("analysis", "election_analysis.txt")

Once this is corrected for each new data set, the results will be similar to the picture below:
![Colorado Election Results](https://user-images.githubusercontent.com/98576235/155270516-971301ab-cbf8-4065-9770-54e055a28652.png)

The code created for the Colorado election can also be used, with some manipulation, to tabulate the electoral college votes during the presidential election. In the .csv file, the format would change to: Column 1: "State", Column 2: "Electoral College Votes", Column 3: "Candidate". The code would then have to be tweaked to change variable names, delete unnecessary code, and add code to count the electoral college votes for each of the candidates, but a solid backbone is provided with the code already created.


