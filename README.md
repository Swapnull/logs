#Logs

##Overview
Logs is a little program that allows you to add a development log to your projects. Each log added to a file will display in the format:
	
	(<log_id>) [<dateadded> <timeadded>] <log> 

Each log file also containts the current id as the first line. Please don't change this number if you go and edit the log by opening the file, if you do then the search functions may not be fully correct.

##Available Commands
###create
Creates a new log file with the name passed in. If you want the file to have an extention this will need to be passed in too.
######format
	logs create -f [name] 
	logs create --file [name]
where [name] is the title of the file. 
*Examples*
	logs create -f develop.log
	logs create --file develop

###insert
Adds a new log by appending it to the end of the specified file. The log must be as a string using _"speech marks"_ . If the file you are trying to insert into does not yet exist then logs will ask if you want to create it. 
######format
	logs insert -f [name] -l "[log]"
	logs insert --file [name] --log "[log]"
where [name] is the tile of the file
where [log] is the log to be added
*Examples*
	logs insert -f develop -l "An exception is thrown when save is pressed"
	logs insert -log "Switch statement not working correctly" -f project.log 

###display
Display will print the last 10 logs inside of a file. If you have more than 10 logs in a file then it will ask if you would like to load the next 10.
######format
	logs display -f [name]
	logs display --file [name]
where [name] is the tile of the file
*Examples*
	logs display -f project.log
	logs diaplay --file develop.log

###find
Find takes in a log id and then displays the log with that id. _There is also plans to do this search by date_
######format
	logs find -f [name] -i [log_id]
	logs find --file [name] --id [log_id]
where [name] is the title of the file
where [log_id] is the integer log id 
*Examples*
	logs find -f project.log -i 14
	logs find --file develop.log --id 194

###delete
Delete takes in a log id and removes the log from the file. Once this has been done it is irreverable so use with care.
	logs delete -f [name] -i [log_id]
	logs delete --file [name] --id [log_id]
where [name] is the title of the file
where [log_id] is the integer log id
*Examples*
	logs delete -f develop -i 3
	logs delete --file project.log --id 27

