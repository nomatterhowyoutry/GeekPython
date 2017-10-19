# 4. Write a script to concatenate N strings.

import random, string

def randomString(length):
   letters = string.ascii_lowercase
   return ''.join(random.choice(letters) for i in range(length))

N = int(input())

tuple = (randomString(random.randint(0,20)) for i in range(0, N))

S = ''.join(tuple)

print(S)