# if you start with $1 and, with each move, you can either double your money or add another $1, what is the smallest
# number of moves you have to make to get to exactly $200?
# Write a program to calculate this and submit the solution with your application.

# It's easy if you go in reverse. Start at 200. Whenever you have an even number,
# divide by 2, otherwise, subtract one. Repeat until you're down to 1, and count the steps.
# its 9 moves
# 1,2,3,6,12,24,25,50,100,200

moves = []
items = []


def recursive_func(n):
    '''This function calculates how many times 2 can be factored into the number entered as argument'''
    # for i in range(1, n + 1):
    #     if n % i == 0 and i % 2 == 0:
    #         moves.append(i // 2)

      







#     # Solutie 1

    if n > 1:
        n = n // 2
        if n % 2 ==0:
            recursive_func(n)
            items.append(n)

#
#     # Solutie 2
#     while n > 1:
#         n //= 2
#         moves.append(n)
#         # else:
#         #     n = (n-1) // 2
#         #     moves.append(n)

#
print(recursive_func(200))
print(moves)
print(items)

# print("List of moves: {}".format(moves))
print("No. of moves: {}".format(len(moves)))
#
factors = []
# items = []
#
#
# def print_factors(x):
#     print("The factors of: ", x, "are: ", )
#     for i in range(1, x):
#         if x % i == 0:
#             factors.append(i)
#     return factors



#
#
#     for j in factors:
#         if j > 1:
#             j //= 2
#             items.append(j)
#
#
# print(print_factors(200))

# print(items)
# mov = []
# def factorial_evens(num):
#     num = 200
#     if num % 2 == 0:
#         product = 1
#         for i in range(1,num+1):
#             i //= 2
#             mov.append(i)
#     return mov

# 
# print(factorial_evens(200))
