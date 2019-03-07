from pathlib import Path # pathlib module is used to make file path parametrs agnostic to windows backslash character
import csv
data_folder = Path('c:/users/avise/desktop/bootcamp/Git/Python-challenge/pybank')
file_path = data_folder / '03-Python_Instructions_PyBank_Resources_budget_data.csv'


# we need a few variables to store/update during the course of reading csv file rows. this program does all required  calculations on the fly while reading individual rows.
# (Not trting to first create an entire new dictionary / list and then use it for our calculations)
# below variables are used
# 'months_count' to keep track of number of months read so far
# 'last_profit'  is the profit in previous month's record (as used to calculate the delta in profit/losses with current month)
# 'total_now'  is the sum of profit/losses for all months records read so far
# 'delta' is the difference between current month's profit/losses and last month's profit/losses
# 'total_delta' is the sum total of all delta's so far
# 'greatest_increase/greatest_decrease/greatest_increase_month/greatest_decrease_month' are variables used to keep track of month/values of greatest +/-ve deltas so far.


months_count = 0
with open(file_path, newline='') as f:
	reader = csv.DictReader(f)
	for row in reader:
		months_count +=1
		
		# first and 2nd months data in csv file would be used to initialize our variables..

		if months_count == 1:
			last_profit = int(row['Profit/Losses'])
			total_now = int(row['Profit/Losses'])
			greatest_increase = 0
			greatest_increase_month =''
			greatest_decrease = 0
			great_decrease_month = ''
			

		elif months_count == 2:
			delta = int(row['Profit/Losses'])-last_profit
			total_now += int(row['Profit/Losses']) 
			total_delta = delta
			last_profit = int(row['Profit/Losses'])
			
			if delta >=0:
				greatest_increase = delta
				greatest_increase_month = row['Date']
			else:
				greatest_decrease = delta
				great_decrease_month = row['Date']
			
		else:
			delta = int(row['Profit/Losses'])-last_profit
			total_now += int(row['Profit/Losses'])
			total_delta += delta
			last_profit = int(row['Profit/Losses'])

			if delta >=greatest_increase:
				greatest_increase = delta
				greatest_increase_month = row['Date']

			if delta < greatest_decrease:
				greatest_decrease = delta
				greatest_decrease_month = row['Date']
				

# writing to textfile "Financial_Analysis.txt
file_path = data_folder / 'Financial_Analysis.txt'
with open(file_path, mode='w') as f:
	
	f.write(f"Financial Analysis\n-------------------\n")
	f.write(f"Total Months: {months_count}\n")
	f.write(f"Total: {total_now}\n")
	f.write(f"Avarage Change: ${total_delta/months_count :6.2f}\n")
	f.write(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})\n")
	f.write(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})\n\n")


# copying file to console as well
print (open(file_path).read())

print(f"FootNote# \n  \n'Average Change' should be averaged over 85 records only,\n as we can not determine change in profit/losses for 1st month\n")
print(f" => {total_delta}/{months_count-1} => {total_delta/(months_count-1):6.2f}")
