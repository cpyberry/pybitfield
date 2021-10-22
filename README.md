# pybitfield

A library that makes it easy to handle bitfield with python

## Requirements

* python 3.6, 3.7, 3.8, 3.9

## Installation

```shell
pip install pybitfield
```

## Usage

When you construct a bitfield with 5 elements, do as follows.

In this case, information up to 5 bits can be stored.

Unless otherwise specified, all bits are 0.

You can use `BitOrder` enumerator class to specify the bit order.

If you want to specify little endian, you should specify `BitOrder.little` in the` bit_order` argument.

```python
from pybitfield import Bitfield, BitOrder


number_of_element = 5
bitfield = Bitfield(number_of_element, bit_order=BitOrder.little)
```

If you want to set the bit, do as follows.

Since the index is zero based, the bitfield stored when running this code is `01111`.

This is the case for big endian.

```python
bitfield.set_bit(0)
bitfield.set_bit(1)
bitfield.set_bit(2)
bitfield.set_bit(3)

# Since the number of elements is 5 and the index is zero-based, a total of 5 index from 0 to 4 can be specified.
# bitfield.set_bit(5)
```

This code remove the 1st and 3rd bits.

This result is `00101`

```python
bitfield.remove_bit(1)
bitfield.remove_bit(3)
```

You can use `is_bit()` to make sure the bit is set.

```python
bitfield.is_bit(1)  # return False
bitfield.is_bit(2)  # return True
```

If you want to convert bitfield to list type, you can use `get_bit_list()`.

The index of bitfield and the index of list correspond.

0 is converted to False, 1 is converted to True.

If you specify little endian, the converted list is reversed.

```python
bitfield.get_bit_list()

# [True, False, True, False, False]
```

If you want to reverse bitfield, you can use `swap_bitfield()`.

The argument represents the bit length.

If you call the method with no arguments, the number of elements in the bitfield is applied to the bit length of the return value.

```python
bitfield.swap_bitfield()
# 20
# 0b10100

bitfield.swap_bitfield(8)
# 160
# 0b10100000

bitfield.swap_bitfield(10)
# 640
# 0b1010000000
```

If you want to convert bitfield to bytes type, you can use `get_bitfield_bytes()`.

If the number of elements in the bitfield is not a multiple of 8, the smallest byte length that can represent it will be applied.

In this case, the number of elements in the bitfield is 5, so the byte length of 1 is applied.

```python
bitfield.get_bitfield_bytes()
# b'\x05'
# 0b00000101
```

If you specify little endian, the a returned array of bytes will be reversed.

```python
bitfield.get_bitfield_bytes()
# b'\xa0'
# 0b10100000
```

## Founder

* [cpyberry](https://github.com/cpyberry)

	email: cpyberry222@gmail.com
