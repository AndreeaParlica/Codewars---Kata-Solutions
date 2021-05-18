# In this Kata you must convert integers numbers from and to a negative-base binary system.
#
# Negative-base systems can accommodate all the same numbers as standard place-value systems, but both positive and negative numbers are represented without the use of a minus sign (or, in computer representation, a sign bit); this advantage is countered by an increased complexity of arithmetic operations.
#
# To help understand, the first eight digits (in decimal) of the Base(-2) system is:
#
# [1, -2, 4, -8, 16, -32, 64, -128]
#
# Example conversions:
#
# Decimal, negabinary
#
# 6,   '11010'
# -6,  '1110'
# 4,   '100'
# 18,  '10110'
# -11, '110101'

from __future__ import print_function

def int_to_negabinary(i):
    if i == 0:
        return 0
    out = []
    while i != 0:
        i, rem = divmod(i, -2)
        if rem < 0:
            i += 1
            rem -= -2
        out.append(rem)
    return "".join(map(str, out[::-1]))


def negabinary_to_int(s):
    if s == "0":
        return 0
    total = 0
    for i, ch in enumerate(s[::-1]):
        total += int(ch) * (-2) ** i
    return total

print(int_to_negabinary(6))
# '11010'
print(int_to_negabinary(-6))
# '1110'
print(negabinary_to_int('11010'))
print(negabinary_to_int('1110'))

