"""
Usage:
    portscan.py host= <host> port= <port>  --tc
    portscan.py host= <host>   begin= <begin>   end= <end>   --scan


Options:
  --tc          try to connect target
  --scan        scan some alaways used ports
  -h --help     Show this screen.
  -v --version     Show version.
"""

from docopt import  docopt
from  socket import  *
import threading
screenlock = threading.Semaphore(1)




class scanRobot:
    def __init__(self,host,port):
          self.host = str(host)
          self.port = int(port)



    def connect(self,hostt,portt):       #Base connect
        setdefaulttimeout(5)
        #print("The greenScaner is connecting %s" % self.host, "please wait......")

        con = socket(AF_INET, SOCK_STREAM)
        con.connect((str(hostt), int(portt)))
        localport = con.getsockname()
        #print("localhost is ", localport)
        return  con



    def connection(self):      #try to connect target

        try:
            con = self.connect(self.host,self.port)
            con.send(("lalallaa\n\r").encode())
            message = con.recv(100)
            if(message):
                print("%s can be connected"%self.host)
            #print(message.decode())
            con.close()
            return  message.decode()
        except:
            print("sorry, can't connect %s" %self.host)
            raise error()





    def scan(self,port):

        try:
            con = self.connect(self.host, port)
            con.send(("hello?\r\n").encode())
            msg = con.recv(1024)
            screenlock.acquire()
            print("\n***************\n\n")
            print("PORT IS ", port)
            print(msg.decode())
        except:
            pass
        finally:
            screenlock.release()


    def scan_some_frquently_used_port(self,begin_port,end_port):     #常用端口扫描, 开始端口和结束端口

        ports = range(begin_port,end_port)
        print(ports)
        for port in ports:
            t = threading.Thread(target=self.scan,args=(port,))
            t.start()











if __name__ == '__main__':
    parases = docopt(__doc__)
    #print(parases["<host>"],parases["<port>"])
    B = scanRobot(parases["<host>"],0)  #实例化对象
    #print(B.port,1)
    if(parases["--tc"]  and  (parases["<host>"])  and   (parases["<port>"]) ):
        #print(1)
        B.port = parases["<port>"]
        print(B.port)
        B.connection()

    if(parases["--scan"]):
        begin= parases["<begin>"]
        end = parases["<end>"]
        B.scan_some_frquently_used_port(int(begin),int(end))
        #print(23)
