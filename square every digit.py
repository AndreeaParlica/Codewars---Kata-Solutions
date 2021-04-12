# Welcome. In this kata, you are asked to square every digit of a number and concatenate them.
#
# For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1.
#
# Note: The function accepts an integer and returns an integer


def square_digits(num):
    nume=[int(i)**2 for i in str(num)]
    string = [str(integer) for integer in nume]
    a_string = ''.join(string)
    return int(a_string)
    



print(square_digits(9119))
# , 811181)