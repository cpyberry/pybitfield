"""
Copyright 2021 cpyberry
https://github.com/cpyberry/pybitfield

cpyberry
email: cpyberry222@gmail.com
github: https://github.com/cpyberry
"""


import math
from enum import Enum, auto


class BitOrder(Enum):
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

	def get_bit_list(self, bit_order=BitOrder.big) -> list:
		"""Return the current bit state as a bool type list.

		Returns:
			list[bool]: True if bit is set, False otherwise.
		"""
		result = []
		for index in range(self.number_of_element):
			result.append(self.is_bit(index))

		if bit_order == BitOrder.little:
			result.reverse()

		return result

	def get_bitfield_bytes(self, bit_order=BitOrder.big) -> bytes:
		"""Convert current bitfield to bytes type.

		Returns:
			bytes: bitfield converted to byte type.
		"""
		byte_length = math.ceil(self.number_of_element / 8)

		if bit_order == BitOrder.big:
			return self.bitfield.to_bytes(byte_length, byteorder="big")
		else:
			bit_length = byte_length * 8
			little_endian_bitfield = self.swap_bitfield(bit_length)
			# It has already been converted to little endian, so return it as it is as big endian.
			return little_endian_bitfield.to_bytes(byte_length, byteorder="big")

	def swap_bitfield(self, length=None) -> int:
		"""Returns the swapped bitfield.

		If 0b10 is specified as an argument, the return value will be 0b01.

		Args:
			length (int, optional): bit length. If None, the current bitfield length is applied. Defaults to None.

		Returns:
			int: swapped bitfield.
		"""
		return self.swap_any_bitfield(self.bitfield, length)

	@classmethod
	def from_bytes(cls, data: bytes, length: int, bit_order=BitOrder.big):
		"""Create an instance of the Bitfield class from the bytes type.

		When the bytes is converted to bitfield, bits which exceed max bit length are removed.

		Args:
			data (bytes): bytes to convert to bitfield.
			length (int): fixed length size of bitfield.
			bit_order (BitOrder, optional): bit order. Defaults to BitOrder.big.

		Returns:
			Bitfield: an instance of the Bitfield class.
		"""
		bitfield = int.from_bytes(data, byteorder="big")

		if bit_order == BitOrder.little:
			bitfield = cls.swap_any_bitfield(bitfield)

		bitfield_bit_length = bitfield.bit_length()

		if bitfield_bit_length > length:
			fitted_bitfield = bitfield >> bitfield_bit_length - length
		else:
			fitted_bitfield = bitfield

		return Bitfield(length, fitted_bitfield)

	@classmethod
	def from_list(cls, bit_bool_list: list, length: int, bit_order=BitOrder.big):
		"""Create an instance of the Bitfield class from the list type.

		When the list is converted to bitfield, bits which exceed max bit length are removed.

		Args:
			base_bool_list (list): list to convert to bitfield.
			length (int): fixed length size of bitfield.
			bit_order (BitOrder, optional): bit order. Defaults to BitOrder.big.

		Returns:
			Bitfield: an instance of the Bitfield class.
		"""
		if bit_order == BitOrder.little:
			bit_bool_list.reverse()

		bitfiled_bit_length = len(bit_bool_list)
		if bitfiled_bit_length > length:
			length = bitfiled_bit_length

		bitfield = Bitfield(length)
		for index, bit_bool in enumerate(bit_bool_list):
			if bit_bool is True:
				bitfield.set_bit(index)
		return bitfield

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

	@staticmethod
	def swap_any_bitfield(bitfield: int, length=None) -> int:
		"""Returns the swapped bitfield.

		If 0b10 is specified as an argument, the return value will be 0b01.

		Args:
			bitfield (int): bitfield you want to swap.
			length (int, optional): bit length. If None, the current bitfield length is applied. Defaults to None.

		Returns:
			int: swapped bitfield.
		"""
		if not length:
			length = len(str(bitfield))

		bitfield_str = format(bitfield, "b")
		swapped_bitfield_str = bitfield_str.zfill(length)[::-1]
		return int(swapped_bitfield_str, 2)
