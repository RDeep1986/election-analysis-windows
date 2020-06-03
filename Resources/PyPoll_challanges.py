
#Open GitHub, and create a new repository and named it election-analysis-windows. Then the gitbash and link the github clone to the desktop.
#download the Excel file from Module section.
#Open the VS code and select open new folder; select the repository folder that is link to Github. It will show all the items in the folder in VS Code.
# create a new file and named it PyPoll_challanges.py
# After providing the file path in our Python script, we will be able to open and read the file
# "r": Open a file to be read.
#"w": Open a file to write to it. This will overwrite an existing file and create a file if one does not already exist.
#"x": Open a file for exclusive creation. If the file does not exist, it will not create one.
#"a": Open a file to append data to an existing file. If a file does not exist, it creates one, if a file has been created the data will be added to the file.
#"+": Open a file for reading and writing.

# first step is to add all the needed and built in libraries. 

import csv
import os #operating system libarary

# now assinge a variable to load a file from the computer path.
#the folder is eletion_analysis_window by using "file_to_load".
#OS will select the file from folder 

file_to_load = os.path.join ("Resources", "election_results.csv") 

#print (file_to_load) this show print the path from the computer where the election_results file is stored.

# After loading the file save the file. 

file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter 

total_votes = 0

#candidate options and candidates votes
candidate_options = [] #this will create a list of candidate 
candidate_votes = {} #this will create the library 

#challanges county option county votes

county_names = [] #this will create a list of counties
county_votes = {} # this will create the library

#Track the winning candidate vote count and percentages in the counties 

winning_candidate = ""
winning_count = 0
winning_percentage = 0
# challenge: Track the largest county voter turnout and its percentage

largest_county_turnout = ""
largest_county_votes = 0

# use th with command to open the file to l=0ad
with open(file_to_load) as election_data:
    reader = csv.reader(election_data) # reader will read the file
    print(reader) # This will show the data

 #Read the header
    header = next(reader) # This will start reading the header form the saved file. 

    #print(header [2])

#loop each roe in the csv file
    for row in reader: # to print the entire row 
        #print (row[2])

#add to the total vote count. We are dding +1 to accumulate 
        total_votes = total_votes + 1 

#get the candidate name from each row
        candidate_name = row[2]

#get the county name from each row
        county_name = row[1]

#if the candidate does not match any esisting candidate 
# add it to the list
        if candidate_name not in candidate_options:

    # add the candidate name to candidate list if the candidate name is mssing 

            candidate_options.append(candidate_name)

    #and begin tracking that candidate voter count

            candidate_votes[candidate_name] = 0

    # add a vote to that candidate count

        candidate_votes[candidate_name] += 1

       # print (candidate_votes) 

       #Add the county_name into county _name folder.
        if county_name not in county_names:
           # add it to the list of county
            county_names.append(county_name) #append is used to add county_name

           #Start tracking the county votes
            county_votes[county_name] = 0

        county_votes[county_name] += 1 #start from 0 and format to increment a variable is by 1.

        #if we print this, that will give number of county votes and 

#save the results to out text file

with open(file_to_save, "w") as txt_file:
    #print the final vote count (to terminal) by using the f' string 

    election_results = (
        f"\nElection Results\n"
        f"------------------\n"
        f"Total Votes{total_votes:,}\n"
        f"------------------\n"
        f"county votes:\n"
    )

    print(election_results, end="")
    txt_file.write(election_results)

    # challenge save final county vote to text file

    for county in county_votes:
        #retrieve vote county and percentage
        county_vote = county_votes[county]
        county_percent = int (county_vote)/int(total_votes) * 100

        county_results = (f"{county}: {county_percent:.1f}% ({county_vote:,})\n")

        print(county_results, end="")

        txt_file.write(county_results)

        # Determine winnign vote
        if (county_vote > largest_county_votes):
            largest_county_votes = county_vote
            largest_county_turnout = county

    #print the cunty with the largest turnout
    largest_county_turnout = ( f"\n----------------------\n"
        f"Largest County Turnout { largest_county_turnout}\n"
        f"-------------------------\n"
    )

    print(largest_county_turnout)
    txt_file.write(largest_county_turnout)

    #save the final cadidate cote count to the text file
    for candidate in candidate_votes:
        #retrieve cote count and percentage
        votes = candidate_votes[candidate]
        vote_percentage = int(votes) / int(total_votes) * 100
        candidate_results =(f"{candidate}: {vote_percentage: .1f}%({votes:,})\n")

        #print each cahdidate coter couynt and percentage to the terminal
        print (candidate_results)
        txt_file.write(candidate_results)
# to finde the winning cadidate 

        if(votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate
            winning_percentage = vote_percentage

    winning_candidate_summary = (f"--------------------\n"
    f"winning: {winning_candidate}\n"
    f"winning Vote Count: {winning_count:,}\n"
    f"-------------------------\n"
    )

    print(winning_candidate_summary)

    #save the winning candidate name to text file
    txt_file.write(winning_candidate_summary)

