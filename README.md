#Logs

##Overview
Logs is a little program that allows you to add a development log to your projects. Each log added to a file will display in the format:
	
	(<log_id>) [<dateadded> <timeadded>] <log> 

Each log file also containts the current id as the first line. Please don't change this number if you go and edit the log by opening the file, if you do then the search functions may not be fully correct.

**Windows users**
I would highly suggest that you download a bash terminal to use logs. It is possible from the command prompt, but logs has only currently been tested with bash(and zsh) so far. Git Bash is a very nice Bash terminal for windows, and gives you the ability to get the project from github easily.

####Usage Requirements
You will need to access the command prompt to use logs. It is only very basic commans that are needed, and I give you them all below. 

##Installation
The installation comes in the 3 parts outlined below. I hope to have these run from a .bat (or .sh) eventually, but for now please refer to the instructions below. 

_If anybody is interested in writing the .bat/.sh files, write them and if they work I will accept a pull request_

######Get logs.py
First of all you need to get the code from the "logs.py" file on github. The easiest way to do this, so long as you have git installed, is to clone the repository:
	
	$ git clone https://github.com/Swapnull/logs.git

Alternatively, you could just copy the code from logs.py and put that anywhere on your system.

######Install python
Currently, you need to have python 2 (I use python 2.7) installed on your computer to use logs. This comes pre-installed on linux and OSX but not on windows.

If you do not have python 2 installed, Go to the [https://www.python.org/download](https://www.python.org/download). 

######Reference logs
To be able to use logs without having to type "python logs.py <command>" every time then you will want to set an alias.

**Windows Command Prompt**
 _I am not 100% sure on windows but some searching brough up this_

From the command line you can make a doskey by running:
	
	doskey logs="python path/to/logs/Release/logs.py"

As stated earlier, I would suggest downloading a bash terminal and then following the linux part.

**Linux**

My preferred way with linux is to edit the file found at /etc/bash.bash_profile . Open this up in a text editor and add the line

	alias logs='python /path/to/logs/Release/logs.py'

**OSX**

With OSX you need to edit the bash_profile command. First of all fire up the terminal.app and then type in:
	
	nano .bash_profile

Once you have this open add the line: 

	alias logs='python /path/to/logs/Release/logs.py'

##Available Commands
###create
Creates a new log file with the name passed in. If you want the file to have an extention this will need to be passed in too.
######Format
	logs create -f [file] 
	logs create --file [file]
where [file] is the title of the file. 
######Examples

	logs create -f develop.log
	logs create --file develop
---
###insert
Adds a new log by appending it to the end of the specified file. The log must be as a string using _"speech marks"_ . If the file you are trying to insert into does not yet exist then logs will ask if you want to create it. 
######Format
	logs insert -f [file] -l "[log]"
	logs insert --file [file] --log "[log]"
where [file] is the title of the file

where [log] is the log to be added
######Examples

	logs insert -f develop -l "An exception is thrown when save is pressed"
	logs insert -log "Switch statement not working correctly" -f project.log 
---
###display
Display will print the last 10 logs inside of a file. If you have more than 10 logs in a file then it will ask if you would like to load the next 10.
######Format
	logs display -f [file]
	logs display --file [file]
where [file] is the title of the file
######Examples

	logs display -f project.log
	logs diaplay --file develop.log
---
###find
There are multiple ways of searching the logs.

####find by id 
Find by id takes in a log id and then displays the log with that id. This should only ever display one result
######Format
	logs find -f [file] -i [log_id]
	logs find --file [file] --id [log_id]
where [file] is the title of the file

where [log_id] is the integer log id 
######Examples

	logs find -f project.log -i 14
	logs find --file develop.log --id 194


####find by date
Find by date takes in a date and then displays all the logs that were made on that date. The date must be put in with the correct format otherwise it will not work.
######Format
	logs find -f [file] -d [date]
	logs find --file [file] --date [date]
where [file] is the title of the file

where [date] is the date in DD/MM/YYYY format
######Examples

	logs find -f project.log -d 01/01/2000
	logs find --file develop.log --date 06/09/2014

####find between dates
Find between dates takes in a date from and a date to string and then displays everything between the two dates, including the dates specified.
######Format
	logs find -f [file] -df [date] -dt [date]
	logs find --file [file] --date-from [date] --date-to [date]
where [file] is the title of the file

where [dategit] is the date in DD/MM/YYYY format
######Examples
	logs find -f project.log -df 01/01/2000 -dt 01/01/2014
	logs find --file develop.log --date-from 01/01/2005 --date-to 31/12/2005
---
###delete
Delete takes in a log id and removes the log from the file. Once this has been done it is irreverable so use with care.
######Format
	logs delete -f [file] -i [log_id]
	logs delete --file [file] --id [log_id]
where [file] is the title of the file

where [log_id] is the integer log id
######Examples

	logs delete -f develop -i 3
	logs delete --file project.log --id 27
---
