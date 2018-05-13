#!/usr/bin/env python

# Server based on https://gist.github.com/marcelom/4218010 "Tiny Python Syslog Server"
# But instead of writing out to a file, it writes to syslog
HOST, PORT = "0.0.0.0", 514

from syslog import syslog, openlog, closelog, LOG_ALERT
import SocketServer

class SyslogUDPHandler(SocketServer.BaseRequestHandler):

    def handle(self):
        data = bytes.decode(self.request[0].strip())
        self.request[1]
        logline = "syslog_server: %s: %s" % (self.client_address[0], str(data))
        print(logline)
        syslog(LOG_ALERT, logline)


if __name__ == "__main__":
    try:
        openlog("syslog_server.py")
        syslog(LOG_ALERT, "syslog_server: Starting up")
        server = SocketServer.UDPServer((HOST,PORT), SyslogUDPHandler)
        server.serve_forever(poll_interval=0.5)
    except (IOError, SystemExit):
        raise
    except KeyboardInterrupt:
        print ("Crtl+C Pressed. Shutting down.")
    finally:
        syslog(LOG_ALERT, "syslog_server: Shutting down")
        closelog()

        