# pybitfield

Pythonでビットフィールドを簡単に扱う為のライブラリ

## 必要環境

* python 3.6, 3.7, 3.8, 3.9

## インストール方法

```shell
pip install pybitfield
```

## 使い方

要素数が5のビットフィールドを構築したい時、以下の様にします。

この場合、最大5ビットの情報を保存できます。

特に指定のない限り、すべてのビットは0クリアされます。

`BitOrder`クラスはビットオーダーを指定したい時に使います。

リトルエンディアンを指定したい場合、`bit_order`引数に`BitOrder.little`を渡してください。

```python
from pybitfield import Bitfield, BitOrder


number_of_element = 5
bitfield = Bitfield(number_of_element, bit_order=BitOrder.big)
```

ビットを設定したい場合は、以下のようにしてください。

インデックスはゼロベースであるため、このコードの実行時に格納されるビットフィールドは `01111`です。

これはビッグエンディアンの場合です。

```python
bitfield.set_bit(0)
bitfield.set_bit(1)
bitfield.set_bit(2)
bitfield.set_bit(3)

# 要素数は5で、インデックスはゼロベースなので、0から4までの合計5つのインデックスを指定できます。
# bitfield.set_bit(5)
```

このコードは1番目と3番目のビットを取り除きます。

この結果は`00101`になります。

```python
bitfield.remove_bit(1)
bitfield.remove_bit(3)
```

`is_bit()`を使えば任意のインデックスのbitがセットされているか調べる事ができます。

```python
bitfield.is_bit(1)  # return False
bitfield.is_bit(2)  # return True
```

`get_bit_list()`を使えばビットフィールドをlist型に変換する事ができます。

ビットフィールドのインデックスと変換後のリストのインデックスは一致しています。

0はFalseに、1はTrueに変換されます。

リトルエンディアンを指定している場合、変換後のリストは逆にされます。

```python
bitfield.get_bit_list()

# [True, False, True, False, False]
```

`swap_bitfield()`を使えばビットフィールドのビット並びを逆にできます。

引数にビット長を指定します。

このメソッドを引数なしで呼び出した場合、戻り値のビット長はビットフィールドの要素数が適応されます。

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

`get_bitfield_bytes()`を使えばビットフィールドをbytes型に変換できます。

ビットフィールドの要素数が8の倍数でない場合、それ表すことができる最小のバイト長が適用されます。

この場合、ビットフィールドの要素数は5なのでバイト長は1が適応されます。

```python
bitfield.get_bitfield_bytes()
# b'\x05'
# 0b00000101
```

リトルエンディアンを指定している場合、返却されるバイト列は逆にされます。

```python
bitfield.get_bitfield_bytes()
# b'\xa0'
# 0b10100000
```

## 創始者

* [cpyberry](https://github.com/cpyberry)

	email: cpyberry222@gmail.com
