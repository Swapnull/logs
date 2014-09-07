import os 
import sys

#-- sys.argv[1] = name of file
#-- sys.argv[2] = log number to be deleted 
def remove_log_message():
	lines = []
	found = False 
	empty = True
	with open(str(sys.argv[1]), 'r') as log_file:
		lines = log_file.readlines()
	with open(str(sys.argv[1]), 'w') as log_file:
		log_file.write(lines[0])
		for line in lines:
			if line[0] == '(':
				x = 1
				log_num = ""
				while(line[x] != ')'):
					log_num += line[x]
					x +=1
				if log_num == sys.argv[2]:
					print "Log has been found.\n"
					found = True
				else:
					log_file.write(line)
					empty = False 
		if found == False:
			print "This Log could not be found."
			empty = False
		if empty == True:
			valid = False
			while(valid == False):
				empty_choice = raw_input("This file is empty, would you like to delete it? (Y/N)").lower()
				if empty_choice == 'y':
					os.remove(sys.argv[1])
					print "file deleted"
					valid = True
				elif empty_choice == 'n':
					valid = True
				else:
					print "Not a valid choice! Try again"

remove_log_message()