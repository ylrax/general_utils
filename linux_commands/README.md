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
	
## Cambiar permisos a todas las carpetas:

    # ver que fichero se van a cambiar
    find . -type d -exec ls -ld {} \;
    
    find . -type d -exec chmod 755 {} \;
    find . -type f -exec chmod 644 {} \;

# Guía para uso de screen

Fuera del screen (en el cluster)
la configuración sale del .screenrc

    screen -S session_name   # crea una sesión llamada session_name, la mía es xarly
    screen -ls               # lista de sesiones activas
    screen -DR               # te mete en la última session
    screen -r session_name   # te mete en la sesion session_name   
    dentro del screen:
    screen -d                # sales de la sesion de screen (pero no borra nada) y vuelves fuera del screen al cluster
    cntl+a d                 # cierra la ventada activa del screen (y pierdes todo)
    cntl+a A                 # renombra la ventana activa del screen
    cntl+a c                 # abre una nueva ventana activa del screen
    cntl+a 1                 # mueve a la ventada 1 del screen
    ...
    cntl+a 9                 # mueve a la ventada 9 del screen
    cntl+a ESC               # entras en modo copia y puedes hacer scroll hacia arrina con las flechas

Comandos más avanzados

    cntl+a S                 # split horizontal de la ventada del screen
    cntl+a |                 # split vertical de la ventada del screen
    cntl+a tab               # cambia region del split de la ventada del screen
    cntl+a X                 # cierra region de la ventada del screen