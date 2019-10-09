#!/usr/bin/python

import argparse

def find_max_profit(prices):
  
  max_profit = 0

  for i in range(len(prices)):
    for j in range(i + 1, len(prices)):
      profit = prices[j] - prices[i]
      if profit > max_profit:
        max_profit = profit


  if max_profit == 0 and profit < 0:
    return profit

  return max_profit



stocks = [100, 90, 80, 50, 20, 10]
stocks2 = [1050, 270, 1540, 3800, 2]

find_max_profit(stocks2)


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))