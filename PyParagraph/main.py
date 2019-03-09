# below code does not use re module
from pathlib import Path

data_folder= Path('C:/Users/avise/Desktop/bootcamp/Git/python-challenge/PyParagraph')
input_files= ['03-Python_ExtraContent_Instructions_PyParagraph_raw_data_paragraph_1.txt', '03-Python_ExtraContent_Instructions_PyParagraph_raw_data_paragraph_2.txt']

reading_from_file = 0
for ifile in input_files:
	reading_from_file += 1

	file_path = data_folder / ifile

	#read passage from file and calculate the passage summary
	with open(file_path, newline = '') as f:
	    text= f.read()
	    total_characters = len(text) # counting total characters in the passage
	    total_letters= total_characters- text.count(',') - text.count('"')- text.count('\n')-text.count('(')-text.count(')')
	    total_words =total_spaces = text.count(' ') # counting spaces in the passages (as approximate number of words)
	    total_sentences = text.count( '.')+text.count( '?')+text.count( '!') # couning number of sentences (as ending with either '!' or '?' or '.')
	    total_paragraphs = text.count('\n') # this in to count number of paragraphs in case there  are more than one paragraphs ()
	    
	
		#writing output files to same folder
	ofile = 'passage_summary'+str(reading_from_file)+'.txt' # naming output file suffixing input file number
	out_file = data_folder / ofile
	
	with open(out_file, mode='w') as f:
		f.write(f'Paragraph Analysis\n')
		f.write(f'------------------\n')
		f.write(f'Approximate Word Count: {total_words}\n')
		f.write(f'Approximate Sentence Count: {total_sentences}\n')
		f.write(f'Average Letter Count: {(total_letters-total_spaces)/total_words:4.1f}\n')
		f.write(f'Average Sentence Length: {total_words/total_sentences}\n')

	# copy output to console as well
	print (open(out_file).read())