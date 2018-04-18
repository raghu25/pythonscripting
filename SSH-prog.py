#Open SSHv2 connection to devices
import paramiko
import time
import re
import sys
#devices = ['10.0.0.1','10.0.0.2','10.0.0.3','10.0.0.4','10.0.0.5','10.0.0.6','10.0.0.7','10.0.0.8','10.0.0.9','10.0.0.10','10.0.0.11','10.0.0.12','10.0.0.13','10.0.0.14','10.0.0.15','10.0.0.16','10.0.0.17','10.0.0.18','10.0.0.19','10.0.0.20','10.0.0.21','10.0.0.22','10.0.0.23','10.0.0.24','10.0.0.25','10.0.0.26','10.0.0.27','10.0.0.28','10.0.0.29','10.0.0.30']
devices = ['10.0.0.30','10.0.0.3']
fd = open ('op1.txt', 'w')
for index, ip in enumerate(devices):
    if index%2 == 0:
		try:
			user_file = sys.argv[1]
			cmd_file = sys.argv[2]
			selected_user_file = open(user_file, 'r')
			selected_user_file.seek(0)
			username = selected_user_file.readlines()[0].split(',')[0]
			selected_user_file.seek(0)    
			password = selected_user_file.readlines()[0].split(',')[1].rstrip("\n")
			session = paramiko.SSHClient()
			session.set_missing_host_key_policy(
					paramiko.AutoAddPolicy())
			session.connect(ip, username = username, password = password)
			connection = session.invoke_shell()	
			selected_cmd_file = open(cmd_file, 'r')
			selected_cmd_file.seek(0)
			for each_line in selected_cmd_file.readlines():
				connection.send(each_line + '\n')
				time.sleep(2)
			selected_user_file.close()
			selected_cmd_file.close()
			output = connection.recv(65535)
			if re.search(r"% Invalid input detected at", output):
				print "* There was at least one IOS syntax error on device %s" % ip
			else:
				print "\nDONE for device %s" % ip 

			old_stdout = sys.stdout
			sys.stdout = fd
			print "\nOutput for device %s" % ip
			print "================================================================="
			print output
			sys.stdout=old_stdout
			session.close()
		except paramiko.AuthenticationException:
			continue
			print "* Invalid username or password. \n* Please check the username/password file or the device configuration!"
			print "* Closing program...\n"
		except:
			continue
fd.close()
fd1 = open ('op1.txt', 'r')
for line in fd1:
    for part3 in line.split():
        if "Output" in part3:
            print line
            print "================================================="			
    for part2 in line.split():
        if "Station" in part2:				
            print line
    for part in line.split(): 
        if "inactive" in part:				
            print line
    for part1 in line.split():
        if "expected" in part1:				
            print line

fd1.close()

