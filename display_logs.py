import os 
import sys

def display_logs():
	if os.path.isfile(sys.argv[1]) == False:
		print "This is not a valid file."
	else:
		with open(str(sys.argv[1]), 'r')as log_file:
			lines = log_file.readlines()
			line_count = 0
			line_count_total = 0
			while((line_count <= 10) and (line_count_total < len(lines))):
				line = lines[line_count_total]
				if line[0] == '(':
					pos = 1
					ident = "ID = "
					date = "Date = "
					log_mes = "Log = "
					while(line[pos] != ')'):
						ident += line[pos]
						pos += 1
					pos +=3
					while(line[pos]!= ']'):
						date += line[pos]
						pos +=1 
					pos +=2
					mes_len = len(line.rstrip())
					while(pos < mes_len):
						log_mes += line[pos]
						pos += 1
					print ident
					print date
					print log_mes
					print '\n'
				line_count +=1
				line_count_total +=1
				if (line_count == 11):
					valid_display_more = False
					while(valid_display_more == False):
						display_more = raw_input("Displayed 10 results. Would you like to display the next 10? (Y/N)").lower()
						if(display_more == 'n'):
							line_count_total = len(lines)+1
							valid_display_more = True
						elif(display_more == 'y'):
							line_count = 0
							valid_display_more = True
						else:
							print "Not a valid choice! Try again"


display_logs()