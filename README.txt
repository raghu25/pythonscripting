SSH-prog.py :

# This is to ssh into network devices using paramiko and gather configuration and bandwidth details and storing them in local drive and also printing the output on command line.






finalscript.py is a secure copy implementation from scp module and paramiko to ssh into wireless network devices and copy specific files (in this case etc/config/wireless) from them.


runs for every minute (can change the frequency of executing time as required)
crontab:
*/1 * * * * cd /home/ra/Desktop/ && /usr/bin/python finalscript.py 2>&1
-----------------------------------------------------------------------------

working_with_files folder contains file parsing scripts using python



