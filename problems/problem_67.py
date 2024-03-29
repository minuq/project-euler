""""
By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom in triangle.txt (right click and 'Save Link/Target As...'), a 15K text file containing a triangle with one-hundred rows.

NOTE: This is a much more difficult version of Problem 18. It is not possible to try every route to solve this problem, as there are 299 altogether! If you could check one trillion (1012) routes every second it would take over twenty billion years to check them all. There is an efficient algorithm to solve it. ;o)
"""
pyramid = open('input/p067_triangle.txt','r')
pyramid = pyramid.read().split("\n")
for i in range(0,len(pyramid)):
    pyramid[i] = pyramid[i].split(" ")

def main():
    i = len(pyramid)-2
    while (i >= 0):
        for j in range(0,len(pyramid[i])):
            pyramid[i][j] = int(pyramid[i][j])
            pyramid[i][j]+=int(max(pyramid[i+1][j],pyramid[i+1][j+1]))
        i -= 1
    print("Problem 67: {0}".format(pyramid[0][0]))
