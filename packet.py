
class Packet:
	def __init__(self):
		self.data = None
		self.ack = None
		self.seq = None
		self.dtype = None

	def __init__(self, data, ack, seq, dtype):
		self.data = data
		self.ack = ack
		self.seq = seq
		self.dtype = dtype





