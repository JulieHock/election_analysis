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
#Open the election results and read the file
with open(file_to_load) as election_data:
    #to do: read and analyze the data here
    #read the file object with the reader function
    file_reader=csv.reader(election_data)
    #print the header row
    headers=next(file_reader)
    print(headers)
#print each row in the csv file
    #for row in file_reader:
       # print(row)
#Using the with statement open the file as a text file
#with open(file_to_save,"w") as txt_file:
    #write some data to the file
    #txt_file.write("Hellow World")
    #Write three counties to the file
    #txt_file.write("Counties in the Election\n--------------------\nArapahoe\nDenver\nJefferson")

