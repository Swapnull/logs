import os
import sys
import datetime

#---- Add these using argparse ---#
#-- Will need to change argv's too? --#
#-m or --message = message
#-f or --file = file to be written to
def add_log_message():
	message = datetime.datetime.now().strftime('[%d/%m/%Y %H:%M.%S] ') + sys.argv[2] + '\n'
	if os.path.isfile(sys.argv[1]) == False:
		valid_create = False
		while(valid_create == False):
			create = raw_input("This file does not exist. Would you like to create it?(Y/N)").lower()
			if create == 'y':
				with open(sys.argv[1], 'w') as new_log:
					new_log.write(str(0) + '\n')
					valid_create = True
			elif create == 'n':
				print "\nPlease pick a valid log file then."
				valid_create = True
			else: 
				print "Not a valid choice!Try again"
	if os.path.isfile(sys.argv[1]):
		with open(str(sys.argv[1]), 'r+') as log_file:
			log_num = log_file.readline()
			next_log_num = str(int(log_num) + 1)
			log_file.seek(0, 0)
			log_file.write(next_log_num)
			log_file.seek(0, 2)
			log_file.write('('+next_log_num+') '+ str(message))
			print "line added to log"

add_log_message()