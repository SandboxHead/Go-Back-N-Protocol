from packet import Packet
from server import Server
from client import Client
from collections import deque
import threading
import random

if __name__=="__main__":
   client1_sent = deque()
   client2_sent = deque()
   client1_received = deque()
   client2_received = deque()
   client1_network = deque()
   client2_network = deque()
   
   client1 = Client(client1_network, client1_sent, client1_received, 1)
   client2 = Client(client2_network, client2_sent, client2_received, 2)

   server1 = Server(client1_sent, client2_received)
   server2 = Server(client2_sent, client1_received)
   
   t1 = threading.Thread(target = client1.start, args=())
   t2 = threading.Thread(target = client2.start, args=())
   t3 = threading.Thread(target = server1.start, args=())
   t4 = threading.Thread(target = server2.start, args=())

   t1.start()
   t2.start()
   t3.start()
   t4.start()

   delay = 0.0025

   while True:
      data1 = random.randint(0, 100)
      data2 = random.randint(100, 200)
      client1_network.append(data1)
      client2_network.append(data2)


