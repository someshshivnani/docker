# docker
how to launch docker on redhat8
ubuntu:14.04 image is used
place in your rhel8 /var/www/cgi-bin
then convert it executable mode by chmod +x 'filename'

give all permission to apache user
'setenforce 0' run this command to disable security

start webserver 'systemctl restart httpd'
disable firewall from redhat as well as form where you will call this script

get ip of redhat and run it in different machines

