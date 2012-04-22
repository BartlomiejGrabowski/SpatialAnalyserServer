import Queue
import threading
import ping
import socket

hosts = ["212.77.100.101", "173.194.70.139", "213.180.141.140",
"127.0.0.1", "195.93.178.6"]

ips = Queue.Queue()

class ThreadUrl(threading.Thread):
    """Threaded DBs time connection measuring"""
    def __init__(self, ips, times):
        threading.Thread.__init__(self)
        self.ips = ips
        self.times = times
        
    def run(self):
        while True:
            #grabs ip from queue
            ip = self.ips.get()
            try:
                delay = ping.do_one(ip, 2000)
            except socket.error, e:
                print "Ping Error:", e               
            self.times[ip] = delay
            print("%s --- %s" % (ip, delay))
            #signals to queue job is done
            self.ips.task_done()

            """abrahama 64/3"""


def main():
    times = {}
    #spawn a pool of threads, and pass them queue instance 
    for i in range(5):
        t = ThreadUrl(ips, times)
        t.setDaemon(True)
        t.start()
    
        #populate queue with data   
    for host in hosts:
        ips.put(host)
 
    #wait on the queue until everything has been processed     
    ips.join()
    
    for key in times.iterkeys():
        print key, times[key]
    

main()


