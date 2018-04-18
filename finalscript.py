#!/usr/bin/python
import paramiko
from scp import SCPClient
devices = ['10.0.0.1','10.0.0.2','10.0.0.3','10.0.0.4','10.0.0.5','10.0.0.6','10.0.0.7','10.0.0.8','10.0.0.9','10.0.0.10','10.0.0.11','10.0.0.12','10.0.0.13','10.0.0.14','10.0.0.15','10.0.0.16','10.0.0.17','10.0.0.18','10.0.0.19','10.0.0.20','10.0.0.21','10.0.0.22','10.0.0.23','10.0.0.24','10.0.0.25','10.0.0.26','10.0.0.27','10.0.0.28','10.0.0.29','10.0.0.30']
remotepath='/etc/config/wireless'
for index, ip in enumerate(devices):
    try:
        localpath='/home/raghu/Desktop/%s' %ip
        if index%2 == 0:
            ssh = paramiko.SSHClient()
            ssh.load_system_host_keys()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(ip, username = 'root', password = 'prabhu')
            with SCPClient(ssh.get_transport()) as scp:
                scp.get(remotepath, localpath)
                print "Finished copying the required file from %s" %ip
                scp.close()
    except paramiko.AuthenticationException:
        print "* Invalid username or password. \n* Please check the username/password for %s or the device configuration!"%ip
    except paramiko.ssh_exception.NoValidConnectionsError:
        print "* No Device with %s address" %ip
        continue

   #     crontab:
    #    * / 1 * * * * cd / home / raghu / Desktop / & & / usr / bin / python
     #   finalscript.py
      #  2 > & 1

        crontab -e = create new cron table


