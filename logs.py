import os
import sys
import datetime
import argparse

class logs:

	def __init__(self):
		self.parserSetup()
		if (os.path.isfile(self.file) == False) and (self.command != "create"):
			if(self.command == "insert"):
				valid_create = False
				while(valid_create == False):
					create = raw_input("This file does not exist. Would you like to create it?(Y/N)").lower()
					if create == 'y':
						self.create()
						valid_create = True
					elif create == 'n':
						print "\nPlease pick a valid log file then."
						valid_create = True
						return
					else: 
						print "Not a valid choice!Try again"
			else:
				print "This file does not exist, please use the create function."
				return


		self.getAction()

	def parserSetup(self):
		#initialise parser
		parser = argparse.ArgumentParser(description= "Logs is a little program that allows you to add a development log to your projects.",
			usage = "logs <command> --file [--log] [--help]")
		
		#add allowed arguments
		parser.add_argument("command")
		parser.add_argument('-f', '--file', help = "", required=True)
		parser.add_argument('-l', '--log', help = "")

		#get arguments passed in
		args = parser.parse_args()
		self.command = args.command
		self.file = args.file
		self.log = args.log
		

	def getAction(self):
		if self.command == "create":
			self.create()
		elif self.command == "insert":
			self.insert()
		elif self.command == "display":
			self.display()
		elif self.command == "find":
			self.find()
		elif self.command == "delete":
			self.delete()

	def create(self):
		print "creating"
		if os.path.isfile(self.file):
			print "A file of this name already exists."
		else:
			with open(self.file, "a") as new_log:
				new_log.write(str(0))

	def insert(self):
		lines = []
		with open(self.file, 'r') as log_file:
			lines = log_file.readlines()
			print lines
			next_log_num = str(int(lines[0]) + 1) 
			lines[0] = next_log_num + '\n'
			log_file.seek(0, 0)
		with open(self.file, 'w') as log_file:
			for line in lines:
				log_file.write(line)
			log_file.write('('+next_log_num+') '+ datetime.datetime.now().strftime('[%d/%m/%Y %H:%M.%S] ') +self.log + '\n')
			print "line added to log"

	def display(self):
		with open(self.file, 'r') as log_file:
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

	def find(self):
		print "finding"

	def delete(self):
		print "deleting"
logs()