#Logs

##Overview
Logs is a little program that allows you to add a development log to your projects. Each log added to a file will display in the format:
	
	(<log_id>) [<dateadded> <timeadded>] <log> 

Each log file also containts the current id as the first line. Please don't change this number if you go and edit the log by opening the file, if you do then the search functions may not be fully correct.

##Available Commands
####create
The create command will create a new log file with the name that is passed in. 

####insert
The insert command will add a new log to the log file that is specified.

####display
The diplay command will display the last 10 logs inside of a file. If you have more than 10 logs in a file then it will ask if you would like to load the next 10.

####find
The find command will take in a log id and then display the log with that id. _There is also plans to do this search by date_

####delete
The delete command will take a log id and remove it from the file. Once this has been done it is irreverable so use with care.

 