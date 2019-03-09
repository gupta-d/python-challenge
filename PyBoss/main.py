# function to get abbreviated state name
def state_abbreviated_name(full_name):
    us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}
    return us_state_abbrev[full_name]

# function to create record in the new format
def reformat_record(row):
    Emp_ID= row[0]
    First_Name = row[1].split(' ', 2)[0] # str.split('splitting chr', max_splits_allowed) will create a list of split strings
    Last_Name = row[1].split(' ', 2)[1]
    DOB = row[2].split('-')[1]+'/'+row[2].split('-')[2]+'/'+row[2].split('-')[0]
    SSN = '***-**-'+ row[3].split('-')[2]
    State = state_abbreviated_name(row[4]) # calling function to get abbreviated state name
    return [Emp_ID,First_Name,Last_Name,DOB,SSN,State]


def main():

    from pathlib import Path # pathlib module is used to make file path parametrs agnostic to windows backslash character
    import csv

    # define data folder and file name for input csv file
    data_folder = Path('c:/users/avise/desktop/bootcamp/Git/Extra/PyBoss')
    input_file = data_folder / '03-Python_ExtraContent_Instructions_PyBoss_employee_data.csv'

    # opening output file and updating its header row as per new format
    output_file = data_folder / 'updated_employees_record.csv'
    f_output= open (output_file, "w", newline="", encoding ="utf8")
    writer = csv.writer(f_output, delimiter=',')
    writer.writerow(['Emp ID','First Name','Last Name','DOB','SSN','State'])

    # open input file and iterate through individual records 
    with open(input_file, newline='') as f_input:
        reader = csv.reader(f_input, delimiter=',')
        csv_header= next(reader) # first row read is header row, subsequent code starts from row 1.
        row_number = 0
        
        for row in reader:  
            row_number += 1
            writer.writerow(reformat_record(row)) # call function to get reformatted record and write to output filr
        
    f_output.close() # close the output file object (as it was not opened using 'with')

main()    