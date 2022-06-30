# The data we need to retrieve
#1. The total number of votes cast
#2. A complete list of candidates who received votes
#3. The percentage of votes each candidate won
#4. The total number of votes each candidate won
#5. The winner of the election based on popular votes
#Add our dependencies
import csv
import os
#Assign a varaible for the file to load and the path
file_to_load=os.path.join("Resources","election_results.csv")
#Assign a variable to save teh file to a path
file_to_save=os.path.join("analysis","election_analysis.txt")
#1. Initialize a total vote counter
total_votes=0
#Candidate Options
candidate_options=[]
#Declare the empty dictionary
candidate_votes={}
#Winning Candidate and Winning Count Tracker
winning_candidate=""
winning_count=0
winning_percentage=0
#Open the election results and read the file
with open(file_to_load) as election_data:
    #to do: read and analyze the data here
    #read the file object with the reader function
    file_reader=csv.reader(election_data)
    #print the header row
    headers=next(file_reader)
    #print(headers)
    #print each row in the csv file
    for row in file_reader:
        #2. Add to the total Vote count
        total_votes+=1
        #3. Print the total votes
        #print(total_votes)
        #print the candidate name from each row
        candidate_name=row[2]
        #If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            #Add it to the list of candidates
            candidate_options.append(candidate_name)
            #Begin tracking that candidates vote count
            candidate_votes[candidate_name]=0
        #Add a vote to that candidates count
        candidate_votes[candidate_name]+=1
#save the results to our text file
with open(file_to_save,"w") as txt_file:
            #Print the final vote count to the terminal
    election_results=(
        f"\nElection Results\n"
        f"_____________________\n"
        f"Total Votes: {total_votes:,}\n"
        f"_____________________\n")
    print(election_results, end="")
    #save the final vote count to the text file
    txt_file.write(election_results)
    #Determine the percentage of votes for each candidate by looping through the counts
    #Iterate through the candidate list
    for candidate_name in candidate_votes:
        #Retrieve vote count of a candidate
        votes=candidate_votes[candidate_name]
        #Calculate teh percentage of votes
        vote_percentage=float(votes)/float(total_votes)*100
        candidate_results=(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        #to do: print out each candidates name, vote count, and percentage of
        #votes to the terminal
        print(candidate_results)
        #save the candidate results to our text file
        txt_file.write(candidate_results)
        #determine winning vote count and candidate
        #determine if the votes is greater than the winning count
        if(votes>winning_count) and (vote_percentage>winning_percentage):
            #if true then set winning_count = votes and winning_percent=vote_percent
            winning_count=votes
            winning_percentage=vote_percentage
            #And set the winning_candidate equal to the candidates name
            winning_candidate=candidate_name
    #print the candidate name and percentage of votes
    #candidate_results=(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
    winning_candidate_summary=(
        f"___________________\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"___________________\n")
    print(winning_candidate_summary)
    #Save teh winning candidates results to the text file
    txt_file.write(winning_candidate_summary)
#print(winning_candidate_summary)
#print the candidate vote dictionary
#print(candidate_votes)
#Using the with statement open the file as a text file
#with open(file_to_save,"w") as txt_file:
    #write some data to the file
    #txt_file.write("Hellow World")
    #Write three counties to the file
    #txt_file.write("Counties in the Election\n--------------------\nArapahoe\nDenver\nJefferson")

