#!usr/bin/python3

print('content-type:text/html')
print()

import subprocess as sp
import cgi

form=cgi.FieldStorage()

osname=form.getvalue('x')

cmd=f'sudo docker run -d -i -t --name {osname} ubuntu:14.04'
output=sp.getstatusoutput(cmd)
status=output[0]

if status==1:
	get_os_ip="sudo docker inspect -f \'{{range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}\' "
	get_os_ip=get_os_ip+osname
	ipadd=sp.getstatusoutput(get_os_ip)
	print("IP Address of your os is "+ipadd[1])		