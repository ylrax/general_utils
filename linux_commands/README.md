# Linux commands

## Free

show the memory usage and the free space

	# in megas:
	free -m

free -m | grep 'Mem:' | awk '{print $2}'


## Cron

Planificator.

	# open the crontab editor:
	crontab -e

Include the codes to execute:


    * * * * * python ~/hello.py
    
    *    *    *    *    *        <command or script to be executed>
    -    -    -    -    -
    |    |    |    |    |
    |    |    |    |    +----- day of week (0 - 6) (Sunday=0)
    |    |    |    +------- month (1 - 12)
    |    |    +--------- day of month (1 - 31)
    |    +----------- hour (0 - 23)
    +------------- min (0 - 59)


every 5 min
*/5 * * * * <command/executable to be executed>
every 10 min
*/10 * * * * <command to be executed>
the minute 5 of each hour
5 * * * * <command to be executed>


## PS

num_procesos_wm_en_ejecucion=`ps -ef | grep WorkflowManager | wc -l | awk '{print $1 - 1}'`


## AWK

awk options program file
	

	# Get the fist column of a csv file
	awk -F, '{print $1}' file.scv


## nohup

El & al final libera la terminal en la que estás trabajando y ejecuta el commando en segundo plano

	nohup <process> <process_params> &

Para ver lo que está haciendo

	cat nohup.out