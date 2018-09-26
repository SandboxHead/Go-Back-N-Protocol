from packet import packet
import random

class Server:
    def __init__(self, sender_data, receiver_data):
        self.sender_data = sender_data
        self.receiveer_data = receiver_data
        self.start_sending()

    def start_sending():
        while True:
            if(size(self.sender_data)):
                curr_data = self.sender_data.popleft()
                delay = random.uniform(0, 1)*0.005
                time.sleep(delay)
                receiver_data.append(curr_data)


