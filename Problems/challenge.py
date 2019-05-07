# HERE ARE THREE BRAIN TWISTERS TO TRY WHILE I AM HOME WITH MY SON WHO IS SICK TODAY...
# PLEASE COMPLETE AT LEAST ONE OF THEM DURING CLASS. (10pts)
# WE WILL GET BACK TO KIVY WHEN WE NEXT MEET (NEXT WEEK)
# EACH PROBLEM IS SOLVABLE BY COMBINING TECHNIQUES FROM CLASS; THEY VARY SLIGHTLY IN DIFFICULTY.



'''
PROBLEM 1
If we take 47, reverse and add, 47 + 74 = 121, which is palindromic.
Not all numbers produce palindromes so quickly. For example,
349 + 943 = 1292,
1292 + 2921 = 4213
4213 + 3124 = 7337
That is, 349 took three iterations to arrive at a palindrome.
Although no one has proved it yet, it is thought that some numbers, like 196, never produce a palindrome.
A number that never forms a palindrome through the reverse and add process is called a Lychrel number.
Due to the theoretical nature of these numbers, and for the purpose of this problem, we shall assume that a number is Lychrel until proven otherwise.
In addition you are given that for every number below ten-thousand, it will either 1) become a palindrome in less than fifty iterations,
or, 2) no one, with all the computing power that exists, has managed so far to map it to a palindrome.
In fact, 10677 is the first number to be shown to require over fifty iterations before producing a palindrome: 4668731596684224866951378664 (53 iterations, 28-digits).
Surprisingly, there are palindromic numbers that are themselves Lychrel numbers; the first example is 4994.
How many Lychrel numbers are there below ten-thousand?
'''


def backward(number):
    forward = str(number)
    backward = ""

    for char in forward:
        backward = char + backward

    return int(backward)

total = 0

for number in range(10000):
    n1 = number
    n2 = backward(number)
    count = 0
    while count < 50 and n1 + n2 != backward(n1 + n2):
        n1 = n1 + n2
        n2 = backward(n1)
        count += 1

    if count == 50:
        #print(number, "is not Lychrel")
        total += 1

print("Solution #1 =", total)

# 249





'''
PROBLEM 2 
The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.
There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
How is the largest circular prime below one million?
'''

def is_prime(n):
    for i in range(2, n//2, 1):
        if n % i == 0:
            return False
    return True

def is_circle_prime(n):
    n1 = str(n)
    for i in range(len(n1)):
        number = n1[i:] + n1[:i]
        if is_prime(int(number)) == False:
            return False
    return True

for i in range(1000000, 0, -1):
    if is_circle_prime(i):
        print("Solution #2 =", i)
        break

# 999331






'''
PROBLEM 3
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
There exists exactly one Pythagorean triplet for which a + b + c = 1000.  What is it?
'''

combo_list = []
for a in range(100, 500):
    for b in range(100, 500):
        for c in range(100, 500):
            if a + b + c == 1000:
                combo_list.append([a, b, c])
    #print(a)



for abc in combo_list:
    #print(abc)
    if (abc[0] ** 2 + abc[1] ** 2) ** 0.5 == abc[2]:
        solution = abc


print("Solution #3 =", solution)

# [375, 200, 425]