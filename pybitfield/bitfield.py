class Bitfield:
	def __init__(self, number_of_element: int, bitfield=0):
		"""
		Args:
			number_of_element (int): fixed length bitfield size.
			bitfield (int, optional): initial value of bitfield. Defaults to 0.
		"""
		self.number_of_element = number_of_element
		self.bitfield = bitfield

	def set_bit(self, index: int) -> None:
		"""Set the bit at the location specified by index.

		The index starts from zero.

		Args:
			index (int): where you want to set the bit.
		"""
		self.bitfield |= self.to_bitfield(index)

	def remove_bit(self, index: int) -> None:
		"""Remove the bit at the location specified by index.

		The index starts from zero.

		Args:
			index (int): where you want to remove the bit.
		"""
		self.bitfield &= ~self.to_bitfield(index)

	@staticmethod
	def to_bitfield(index: int) -> int:
		"""Return a bitfield with a bit at the position specified by index.

		The index starts from zero.

		Args:
			index (int): where you want to set the bit.

		Returns:
			int: the bitfield.
		"""
		return pow(2, index)
