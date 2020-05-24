#!/usr/bin/python

import argparse

def find_max_profit(prices):
  # get the most profit that can be made from subtracting on of the numbers that came before any number in the list 
  # iterate through the numbers in the list 
  # for each number, that number will be used to subtract from every following number in the list 
  # so you'll need to iterate through the rest of the list past the current number 
  # every time you do one of those subtractions check if the result is lower than a counter
  # if it is lower, then replace the counter
  low = prices[1]-prices[0]
  for i in range(1, len(prices)):
    for j in range(0, i):
      a = prices[i]
      b = prices[j]
      # print(f'{a}-{b}=',a-b)
      if (a-b)>low: 
        low = a-b
  return low

# prices = [100, 90, 80, 50, 20, 10]
# print(prices)
# print(prices[1:len(prices)])
# print(prices[0:len(prices)-1])

# find_max_profit(prices)


# if __name__ == '__main__':
#   # This is just some code to accept inputs from the command line
#   parser = argparse.ArgumentParser(description='Find max profit from prices.')
#   parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
#   args = parser.parse_args()

#   print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))