# nthPronicNumber(n) [20 pts]
# Write the function nthPronicNumber that takes a non-negative int n and returns the nth Pronic
# Number. Pronic number is a number which is the product of two consecutive integers, that is, a
# number n is a product of x and (x+1).

def nthpronicnumber(n):
	# Your code goes here
 import math
#rangenumber=int(input(n))
c = 0
letest = 0
num = 1
while c != nthpronicnumber:
    flag = 0
    for j in range(0, num + 1):
        if j * (j + 1) == num:
            flag = 1
            break
    if flag == 1:
            c+=1
            letest = num

    num = num + 1
    #print(rangenumber,"th Pronic number is ",letest)
pass
