from functools import reduce
from operator import mul

def readFile(name):
  with open(name, 'r') as f:
    content = [[ 1 if char == "#" else 0 for char in line.rstrip()] for line in f.readlines()]
  return content

def findElements(arr, right, down):
  return sum([ arr[i][(i / down * right) % len(arr[0])] for i in range(0, len(arr), down)])

def findTotalElements(arr, coords):
  res = [findElements(arr, cx, cy) for cx, cy in coords]
  return reduce(mul, res, 1)
