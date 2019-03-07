from pathlib import Path # pathlib module is used to make file path parametrs agnostic to windows backslash character
import csv # using csv.DictReader to read rows in dictionary format

# assigning input file path
data_folder = Path('c:/users/avise/desktop/bootcamp/Git/python-challenge/pypoll')
file_path = data_folder / '03-Python_Instructions_PyPoll_Resources_election_data.csv'

# csv file contains 3 columns "Voter ID", "County", "Candidate"

total_votes=0 # keeping track of votes casted through iteration
results={} # results will be stored/updated in this dictionary through iteration{"candidate name":votes}
with open(file_path, newline='') as f:
	reader = csv.DictReader(f)
	for row in reader:
		total_votes += 1
		
		if row['Candidate'] in results.keys(): 
			results[row['Candidate']] += 1
		else:
			results.update({row['Candidate'] : 1})
#print(results)


# writing formatted results on "Election_Result.txt" file

file_path = data_folder / 'Election_Results.txt'
with open(file_path, mode='w') as f:

	f.write(f"Election Results\n--------------------------\n")
	f.write(f"Total Votes: {total_votes}\n--------------------------\n")
	for candidate in results.keys():
		f.write(f"{candidate:}: {100*(results[candidate]/total_votes):.3f}% ({results[candidate]})\n")
	f.write(f"--------------------------\n")
	f.write(f"Winner: {max(results, key=results.get)}\n")
	f.write(f"--------------------------")

# copying same file to console
print(open(file_path).read())


