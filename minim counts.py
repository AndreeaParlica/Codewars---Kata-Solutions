# if you start with $1 and, with each move, you can either double your money or add another $1, what is the smallest
# number of moves you have to make to get to exactly $200?
# Write a program to calculate this and submit the solution with your application.


moves = []
def moves_count(n):
    while n > 1:
        if n % 2 == 0:
            n = n // 2
        elif n == 3 or n % 4 == 1:
            n = n - 1
        else:
            n = n + 1
        moves.append(n)
    return "Numbers of moves: {}".format(len(moves))

print(moves_count(200))
print(moves)