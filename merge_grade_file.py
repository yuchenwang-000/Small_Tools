'''
This program can help you to merge csv grade files from myCourse and Perusall,
You need to provide both .csv file name, and the corresponding grade column in those
two files.

This program will iterate each tuple from myCourse csv file, get the student email address and
find the corresponding student by email address in the Perusall csv file, then get the grade from
the Perusall csv file, and add it to myCourse csv file. 

'''

import pandas as pd
import csv

'''
Please enter the file name and the grade column number at here
Please note that the grade column count starts from 0
----- modify here -----
'''
myCourse_file = 'mycourse.csv'
grade_index_mycourse = 3

perusall_file = 'gradebook.csv'
grade_index_perusall = 3

'''-----You usually do not need to modify code below this line-----'''

# convert myCourse csv file to dictionary
def file_to_dict_mycourse(file_name):
	reader = csv.reader(open(file_name))
	result = {}
	for row in reader:
		key = row[0] #the key value (email) from csv, here it is from number 0 column
		if key in result:
			pass
		result[key] = row[1:]
	#print(result)
	return result

# convert Perusall file to dictionary
def file_to_dict_perusall(file_name):
	reader = csv.reader(open(file_name))
	result = {}
	for row in reader:
		key = "#" + row[2] #the key value (email) from csv, here it is from number 2 column
		if key in result:
			pass
		result[key] = row[1:]
	#print(result[key])
	return result

# get field name of the csv file
def get_field_name(file_name):
	with open(file_name, 'r') as f:
		d_reader = csv.DictReader(f)
		#get fieldnames from DictReader object and store in list
		headers = d_reader.fieldnames
	return headers

mycourse_dict = file_to_dict_mycourse(myCourse_file)
perusall_dict = file_to_dict_perusall(perusall_file)

# write to output file
for key, value in mycourse_dict.items():
	if key in perusall_dict:
		perusall_tuple = perusall_dict.get(key)
		value[grade_index_mycourse] = perusall_tuple[grade_index_perusall]

'''for key, value in mycourse_dict.items():
	print(key)
	print(value)'''

field_name = get_field_name('mycourse.csv')

(pd.DataFrame.from_dict(data=mycourse_dict, orient='index')
   .to_csv('dict_file.csv', header=False))

