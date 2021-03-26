from itertools import combinations
from functools import reduce
from operator import mul

def readFile(name):
  with open(name, 'r') as f:
    content = [int(line) for line in f.readlines()]
  return content

def findElements(arr, matcher, numElements):
  return [ (list(seq), reduce(mul, seq, 1)) for seq in combinations(arr, numElements) if sum(seq) == matcher ]
