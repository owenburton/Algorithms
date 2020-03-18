#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution
# def eating_cookies(n, cache=None):
  # how to find all possible ways a list of numbers ([1,2,3]) go into a number
  # they want you to solve it recursively, so what's your base case?
  # base case: zero cookies or negative cookies
  # if n<1:
  #   return # something
  # pass

  # floor divide n by each num in your list and save those as variables 
  # write our condition equation (1*var1 + 2*var2 + 3*var3)==n
  # get every combination of (1*(nums in range(var1)) + 2*(nums in range(var2)) + 3*(nums in range(var3))) where
  # that combination is equal to n 
  # after that get every possible order of each of those found combinations

def eating_cookies(n):
  if n<0:
    return 0
  elif n==0:
    return 1
  return eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3)
  # var1 = n # bc n//1 is the same as just n
  # var2 = n//2
  # var3 = n//3
  # lis = []
  # for a in range(var1,-1,-1):
  #   for b in range(var2,-1,-1):
  #     for c in range(var3,-1,-1):
  #       if (a + 2*b + 3*c)==n:
  #         lis.append([1]*a + [2]*b + [3]*c)

          # get_all_combos_of([1]*a + [2]*b + [3]*c)
    
          # for combo in combos:
          #   if combo not in lis:
          #     lis.append(combo)

          # print(f'1*{a} + 2*{b} + 3*{c} == {n}')

# eating_cookies(5)

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')