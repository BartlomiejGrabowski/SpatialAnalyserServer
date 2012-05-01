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
        hosts = ["212.77.100.101", "173.194.70.139", "213.180.141.140",
                "127.0.0.1", "195.93.178.6"]

        #spawn a pool of threads, and pass them queue instance 
        for i in range(5):
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
        best_ip = self.get_best_ip()
        if best_ip == '127.0.0.1':
            self.db = 'local_db'
            self.user = 'postgres'
            self.passwd = 'postgres'
        elif best_ip == '212.77.100.101':
            self.db = 'target_db_1'
            self.user = 'postgres'
            self.passwd = 'postgres'
        elif best_ip == '173.194.70.139':
            self.db = 'target_db_2'
            self.user = 'postgres'
            self.passwd = 'postgres'
        elif best_ip == '213.180.141.140':
            self.db = 'target_db_3'
            self.user = 'postgres'
            self.passwd = 'postgres'
        elif best_ip == '195.93.178.6':
            self.db = 'target_db_4'
            self.user = 'postgres'
            self.passwd = 'postgres'
        else:
            raise "Unknown database parameters!"
        
    
if __name__ == "__main__":    
    ips = Queue.Queue()   
    times = {}

    obj = FindDB(ips, times)
    obj.get_best_ip()


