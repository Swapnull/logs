import os 
import sys 

#-- sys.argv[1] should be the name of the file

def create_log():
	name = sys.argv[1]
	if os.path.isfile(name):
		print "A file of this name already exists."
	else:
		with open(name, 'w') as new_log:
			new_log.write(str(0) + '\n')

create_log()