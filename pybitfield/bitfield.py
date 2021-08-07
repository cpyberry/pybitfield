class Bitfield:
	def __init__(self, number_of_element: int, bitfield=0):
		"""
		Args:
			number_of_element (int): fixed length bitfield size.
			bitfield (int, optional): initial value of bitfield. Defaults to 0.
		"""
		self.number_of_element = number_of_element
		self.bitfield = bitfield
