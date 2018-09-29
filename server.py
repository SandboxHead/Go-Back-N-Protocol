from packet import Packet
import random
import time
from collections import deque

class Server:
    def __init__(self, sender_data, receiver_data):
        self.sender_data = sender_data
        self.receiveer_data = receiver_data

    def start(self):
        while True:
            if(len(self.sender_data)):
                curr_data = self.sender_data.popleft()
                err = random.uniform(0, 1)
                if(curr_data == 0 and err<0.1): continue
                elif(curr_data.dtype==1 and err<0.05): continue
                delay = random.uniform(0, 1)*0.005
                time.sleep(delay)
                receiver_data.append(curr_data)
            time.sleep(1)
            print ("server_here")

