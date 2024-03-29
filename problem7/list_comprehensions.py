'''
You are given three integers x, y and z representing the dimensions of a cuboid
along with an integer n. Print a list of all possible coordinates given by
(i, j, k) on a 3D grid where the sum of i+j+k is not equal to n.
Here, 0<=i<=x; 0<=j<=y; 0<=k<=z.
Please use list comprehensions rather than multiple loops, as a learning exercise.

Input Format:

Four integers x, y, z and n, each on a separate line.

Constraints:

Print the list in lexicographic increasing order.
'''


x = int(input("Enter the x value: "))
y = int(input("Enter the y value: "))
z = int(input("Enter the z value: "))
n = int(input("Enter the n value: "))


cuboid_dimensions = [[i, j, k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if (i+j+k) != n]
print(cuboid_dimensions)
