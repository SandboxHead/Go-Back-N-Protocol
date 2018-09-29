from packet import Packet
from collections import deque
import time
import sys
class Client:
    def __init__(self,network_data, sent_data, received_data):
        self.frame = None
        self.network_data = network_data
        self.ack_expected = 0
        self.next_frame_to_send = 0
        self.frame_expected = 0
        self.nbuffered = 0
        self.buffer = [None] * 7
        self.event = -1
        self.network_layer_ready = 1
        self.sent_data = sent_data
        self.received_data = received_data
        self.timer = [sys.maxsize] * 7
    def start(self):
        while(True):
            if(len(self.network_data) > 0):     # network_layer_ready
                self.buffer[self.next_frame_to_send] = network_data.popleft()
                nbuffered += 1
                self.send_data()
                self.next_frame_to_send += 1
                self.next_frame_to_send %= 7
            
            elif(len(self.received_data) > 0):
                self.frame = self.received_data.popleft()
                if(self.frame.seq == self.frame_expected):
                    self.frame_expected += 1
                    self.frame_expected %= 7
                    self.send_acknowledgement()
                while(self.between(self.ack_expected,self.frame.ack, self.next_frame_to_send)):
                    self.nbuffered -= 1
                    self.timer[ack_expected] = None
                    self.ack_expected += 1
                    self.ack_expected %= 7

            elif(time.time()-self.timer[self.ack_expected] > 1):
                self.next_frame_to_send = self.ack_expected
                for i in range(1,self.nbuffered+1):
                    self.send_data()
                    self.next_frame_to_send += 1
                    self.next_frame_to_send %= 7
                    
            time.sleep(1)
            print ("client_here")
    def between(self,a,b,c):
        if ((a<=b and b<c) or (c<a and a<=b) or (b<c and c<a)):
            return True
        return False
        
    def send_data(self):
        self.frame.data = self.buffer[next_frame_to_send]
        self.frame.seq = next_frame_to_send
        self.frame.ack = (frame_expected + 7) % 8
        self.frame.dtype = 0
        self.sent_data.append(self.frame)
        self.timer[next_frame_to_send] = time.time()

    def send_acknowledgement(self):
        self.frame.data = self.buffer[(next_frame_to_send + 7)%8]
        self.frame.seq = (next_frame_to_send + 7)%8
        self.frame.ack = (frame_expected + 7) % 8
        self.frame.dtype = 1
        self.sent_data.append(self.frame)
