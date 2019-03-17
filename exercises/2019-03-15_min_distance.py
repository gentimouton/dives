# Question 12 - Finding the value closest to 0
# You are given a list of Q 1D points, return the value in Q that is the closest to value j.
# Example:
# Q = [1, -1, -5, 2, 4, -2, 1]
# j = 3
# The answer in this case 2.


q = [1, -1, -5, 2, 4, -2, 1]
j = 3

t = min(
    zip(
        q,
        map(lambda x: abs(x-j), q)  # compute distance
    ),
    key=lambda tup: tup[1]  # find tuple with smallest second element
)[0]
print(t)
