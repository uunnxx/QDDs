# Given an integer, return the integer with reversed digits.
# Note: The integer could be either positive or negative.

def solution(x):
    string = str(x)

    if string[0] == '-':
        return int('-'+string[:0:-1])
    else:
        return int(string[::-1])


print(solution(-231))
print(solution(345))


def solution_2(num):
    if num < 0:
        # return int(f"-{string[:0:-1]}")
        return int(f"-{str(abs(num))[::-1]}")

    return int(str(num)[::-1])


print(solution_2(-123))
print(solution_2(123))
