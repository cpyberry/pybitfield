"""
Copyright 2021 cpyberry
https://github.com/cpyberry/pybitfield

cpyberry
email: cpyberry222@gmail.com
github: https://github.com/cpyberry
"""


import math
from enum import Enum, auto


class ByteOrder(Enum):
	big = auto()
	little = auto()


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

	def is_bit(self, index: int) -> bool:
		"""Check if the bit specified by index is set.

		Args:
			index (int): Where you want to find out if a bit is setting.

		Returns:
			bool: True if bit is set, False otherwise.
		"""
		return self.bitfield & self.to_bitfield(index) != 0

	def get_bit_list(self) -> list[bool]:
		"""Return the current bit state as a bool type list.

		Returns:
			list[bool]: True if bit is set, False otherwise.
		"""
		result = []
		for index in range(self.number_of_element):
			result.append(self.is_bit(index))
		return result

	def get_bitfield_bytes(self, byteorder=ByteOrder.big) -> bytes:
		"""Convert current bitfield to bytes type.

		Returns:
			bytes: bitfield converted to byte type.
		"""
		length = math.ceil(self.number_of_element / 8)

		# self.bitfield stores bitfield like littile endian.
		# If the first bit is 0, the second bit is 1, and the third bit is 1, it is stored as 0b110.
		if byteorder == ByteOrder.big:
			return self.bitfield.to_bytes(length, byteorder="little")
		else:
			return self.bitfield.to_bytes(length, byteorder="big")

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
