#!/usr/bin/python

import sys

def rock_paper_scissors(n):
  c = 3**n # number of permutations
  rps = [[]] * c
  choices = {'r':'p','p':'s','s':'r'}

  def p_fn(n,x,choice):
    if n==1:
      return [choices[choice]]
    c1 = choices[choice]
    c2 = choices[c1]
    c3 = choices[c2]
    # print(c1,c2,c3)
    x -= 1
    rps[x-3] = rps[x-3] + p_fn(n-1,x,c1)
    rps[x-2] = rps[x-2] + p_fn(n-1,x,c2)
    rps[x-1] = rps[x-1] + p_fn(n-1,x,c3)
  
  # print(rps)
  if n==0:
    return rps
  rps[c-3] = rps[c-3] + p_fn(n,c,'s')
  rps[c-2] = rps[c-2] + p_fn(n,c,'r')
  rps[c-1] = rps[c-1] + p_fn(n,c,'p')
  # print(rps)
  return rps


# def add_one_more(list_plays):
#     list_return =[]
#     strings = [[‘rock’],[‘paper’],[‘scissors’]]
#     for i in list_plays:
#         for j in strings:
#             list_return.append(i + j)
#     return list_return

# def rock_paper_scissors(n):
#     #strings = [[‘rock’],[‘paper’],[‘scissors’]]
#     if n <= 0:
#         return [[]]
#     else:
#         return add_one_more(rock_paper_scissors(n-1))


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')