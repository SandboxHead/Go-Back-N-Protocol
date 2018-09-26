from packet import Packet
from collections import deque
import time
class Client:
    def __init__(self,network_data,mac_data):
        self.frame = None
        self.network_data = network_data
        self.ack_expected = 0
        self.next_frame_to_send = 0
        self.frame_expected = 0
        self.nbuffered = 0
        self.buffer = [None] * 7
        self.event = -1
        self.network_layer_ready = 1
        self.mac_data = mac_data
        self.timer = [None] * 7
        self.start()
    def start(self):
        while(True):
            if(event == 0):     # network_layer_ready
                self.buffer[self.next_frame_to_send] = network_data.popleft()
                nbuffered += 1
                self.send_data()
                self.next_frame_to_send += 1
                self.next_frame_to_send %= 7

    def send_data(self):
        self.frame.data = self.buffer[next_frame_to_send]
        self.frame.seq = next_frame_to_send
        self.frame.ack = (frame_expected + 7) % 8
        self.mac_data.append(self.frame)
        self.timer[next_frame_to_send] = time.time()


