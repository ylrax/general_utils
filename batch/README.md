# Interesting batch launch scripts


## sed

Do data modification according to some rules and split out in the STOUT

### Usage

	# Directly:
	sed <options> <file>
	# Indirectly
	cat <file> | sed <options>
	#example
	echo "This is awesome" | sed 's/awesome/legen-dary/'

### Commmand functionalities

	# remove lines (2 and 4 for example) (also pattern avalilable)
	sed 'd2,4' <file>

	# substitute lines (the sixth one for example)
	sed '6c\New line text' <file>

	# Show only the changed ones with the paramenter -n
	sed -n '6c\New line text' <file>

	# substitute test
	sed 's/text/replacement/' <file>
	# Substitute text on a certain match number
	sed 's/text/replacement/<number>' <file>
	# Limit the rows modified (6 for example)
	sed '<number>s/text/replacement/' <file>
	# or apply from a line to the end (6 for example)
	sed '<number>,$s/text/replacement/' <file>

	# insert (with the insert i or append a, one is after and other is before the output)
	sed 'a\text' <file>

	# write some text at the beggining of each line
	sed 's/^/<text>/' <file>

	# Patter search....
	# and more

	# it can be saved into a file and apply it 
	$ echo "show databases" | mysql -u pafuser | sed -f subrayado.sed
	# it can show it in two columns, hightlyt stuff, filter...


## See permitions numbers

	stat -c "%a %n" <path>

## Jobs and ps

jobs: Displays status of jobs in the current shell session.

	# Example
	sleep 100 &
	jobs -l    # shows: jobID PID status name

ps: Displays the process in the system

	ps
	# and there is billios of ways to show and filter it...

## Nohup

Stands for "no hangup." The hangup (HUP) signal, which is normally sent to a process to inform it that the user has logged off (or "hung up"), is intercepted by nohup, allowing the process to continue running.

By default, the standard output (stdout) will be redirected to nohup.out file in the current directory if possible, or $HOME/nohup.out otherwise. And the standard error (stderr) will be redirected to stdout, thus it will also go to nohup.out. So, the nohup.out will contain both standard output and error messages from the script executed with nohup command. 

	nohup <mycommand> &
	# it returns  the process ID (PID) and it can be killed with:
	kill -9 <PID>
	# to specity the output file you have to use the >
	nohup <mycommand> > <file> &
	# monitor the process
	ps aux | grep <file> 




## Dates

The Date and Time raw format depends on what you've specified in the Region and Language Control Panel 

### Today's date

	date /t
	# a environment variable contains it:
	echo %date%

	# in MM/DD/YYYY format
	for /F "tokens=2" %i in ('date /t') do echo %i

### Days from a date 

	startDate='2016-01-01'
	days_to_process=$(( ($(date +%s) - $(date --date=$startDate +%s) )/(60*60*24) ))
	# you can add extra days
	days_to_process=$(( ($(date +%s) - $(date --date=$startDate +%s) )/(60*60*24) +5 ))

### Add days to a date

	startDate='2016-01-01'
	for i in $(seq 0 $days_to_process)
	do
	echo $(date -I -d "$startDate +$i days")
	done

### time

	time /t

	# a environment variable contains it:
	echo %time%


### Date split

	# Both
	echo  %date%-%time%
	set day=%date:~7,2%
	set month=%date:~4,2%
	set year=%date:~10,4%
	set today=%year%%month%%day%


## Modify format:

	for /f "tokens=2 delims==" %%a in ('wmic OS Get localdatetime /value') do set "dt=%%a"
	set "YY=%dt:~2,2%" & set "YYYY=%dt:~0,4%" & set "MM=%dt:~4,2%" & set "DD=%dt:~6,2%"
	set "HH=%dt:~8,2%" & set "Min=%dt:~10,2%" & set "Sec=%dt:~12,2%"

	set "fullstamp=%YYYY%%MM%%DD%%HH%%Min%%Sec%"

	# %dt:~0,4% notation: means 4 positions from the string beggining in 0


## EG previous month

	@echo off
	setlocal
	for /f %%A In ('wmic os get localDateTime') do for %%B in (%%A) do set ts=%%B
	set /a "YYYY=%ts:~,4%, MM=1%ts:~4,2%, DD=%ts:~6,2%"
	if %MM% Equ 101 (set /a "YYYY-=1, MM=112") else set /a "MM-=1"
	set "prevMonth=%YYYY%%MM:~1%"
	echo %prevMonth%%DD%

## Full loop example:

	@echo off
	echo "Lanzando proceso con lista de fechas"

	for /f "tokens=2 delims==" %%a in ('wmic OS Get localdatetime /value') do set "dt=%%a"
	set "YY=%dt:~2,2%" & set "YYYY=%dt:~0,4%" & set "MM=%dt:~4,2%" & set "DD=%dt:~6,2%"
	set "HH=%dt:~8,2%" & set "Min=%dt:~10,2%" & set "Sec=%dt:~12,2%"

	set "fullstamp=%YYYY%%MM%%DD%%HH%%Min%%Sec%"

	rem set "processDates=2018-11-09 2018-11-10 2018-11-11 2018-11-12 2018-11-13 2018-11-14 2018-11-15 2018-11-16"
	set "processDates=2018-11-09 2018-11-10 2018-11-11 2018-11-12"

	for %%i in (%processDates%) do (
		echo %%i)


## Basic execution exit logs:


	sh program.sh;

	result=$?
	if [ "$result" != 0 ]
	then
		echo "Error: ..............."
		echo "Script exit"
		exit 1
	else
		echo "Script launched correctly"
		exit 0
	fi

