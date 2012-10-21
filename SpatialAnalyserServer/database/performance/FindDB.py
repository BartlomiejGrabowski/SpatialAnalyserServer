import Queue
import threading
import ping
import socket
import operator



class FindDB(threading.Thread):
    """Threaded DBs time connection measuring"""
    def __init__(self, ips, times):
        threading.Thread.__init__(self)
        self.ips = ips
        self.times = times
        
    def run(self):
        average_time = 0;
        while True:
            #grabs ip from queue
            ip = self.ips.get()
            try:
                #get average value from 5 times.
                for i in range(5):
                    delay = ping.do_one(ip, 2000)
                    average_time += delay;
            except socket.error, e:
                print "Ping Error:", e               
            self.times[ip] = average_time/5;
            
            #signals to queue job is done
            self.ips.task_done()


    def get_db_delay(self):
        hosts = ["192.168.1.102"]

        #spawn a pool of threads, and pass them queue instance 
        for i in range(2):
            t = FindDB(self.ips, self.times)
            t.setDaemon(True)
            t.start()
        
        #populate queue with data   
        for host in hosts:
            self.ips.put(host)
     
        #wait on the queue until everything has been processed     
        self.ips.join()
        
        return self.times

    def get_best_ip(self):
        #Function returns ip address with minimum delay value.
        delay_list = self.get_db_delay()
        #sort dictionary from get_db_delay() function
        sorted_list = sorted(delay_list.iteritems(), key=operator.itemgetter(1))
        #return first element of list (min delay value).
        best_ips = [item[0] for item in sorted_list]
        return best_ips.__getitem__(0)
    
    def set_conn_parameters(self):
        self.best_ip = self.get_best_ip()
        if self.best_ip == '192.168.1.102':
            self.db = 'shp_database'
            self.user = 'postgres'
            self.passwd = 'postgres'
        #elif self.best_ip == '192.168.1.101':
        #    self.db = 'gis_db'
        #    self.user = 'postgres'
        #    self.passwd = 'postgres'
        else:
            raise "Unknown database parameters!"
        
    
if __name__ == "__main__":    
    ips = Queue.Queue()   
    times = {}

    obj = FindDB(ips, times)
    print(obj.get_best_ip())
