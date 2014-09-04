import os
import sys

def find_log_message():
	if os.path.isfile(sys.argv[1]) == False:
		print "This is not a valid file"
	else:
		lines = []
		found = False
		empty = True
		with open(str(sys.argv[1]),'r')as log_file:
			lines = log_file.readlines()
			for line in lines:
				if line[0] == '(':
					pos= 1
					log_num= ''
					while(line[pos] != ')'):
						log_num += line[pos]
						pos += 1
					if log_num == sys.argv[2]:
						ident = "ID = " + sys.argv[2]
						date = "Date = "
						log_mes = "Log = "
						pos +=3
						while(line[pos] != ']'):
							date += line[pos]
							pos += 1
						pos += 2
						mes_len = len(line.rstrip())
						while(pos < mes_len):
							log_mes += line[pos]
							pos += 1
						print ident
						print date
						print log_mes
						print '\n'

find_log_message()