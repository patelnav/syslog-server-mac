# syslog-server-mac
Recieve syslog messages on UDP 514 and log them into syslog

## Background
My Asus router (RT-N18U) as a "Remote Log Server" option. This sends syslog messages to the UDP 514 port. 
Enabling the server portion of syslogd required [System Integrity Protection (SIP)](https://en.wikipedia.org/wiki/System_Integrity_Protection) to be turned off,
and a bunch of other shenanigans.

This script needs to be executed with sudo (bad), but it just works (good!)

## Credit
[Marcelo](https://gist.github.com/marcelom)'s [pysyslog.py](https://gist.github.com/marcelom/4218010)
