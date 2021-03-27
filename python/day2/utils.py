from itertools import combinations
from functools import reduce
from operator import mul
import re
import math

def flatten(l):
  return (item for sublist in l for item in sublist)

def readFile(name):
  p = re.compile(r'(\d+)\-(\d+) (\w): (\w+)')
  with open(name, 'r') as f:
    content = [p.findall(line) for line in f.readlines()]
  return flatten(content)

def validate(line):
  minOccurrence = int(line[0]) if line[0] is not None else 0
  maxOccurrence = int(line[1]) if line[1] is not None else math.inf
  if not line[2]:
    return True
  
  count = line[3].count(line[2])
  return minOccurrence <= count and maxOccurrence >= count

def findElements(arr):
  return [line for line in arr if len(line) and validatePart2(line)]

def validatePart2(line):
  li = int(line[0]) - 1 if line[0] is not None else 0
  ri = int(line[1]) - 1 if line[1] is not None else 0
  if li < 0 or ri < 0 or not line[2]:
    return False
  
  password = line[3]
  char = line[2]
  return (password[li] == char and not password[ri] == char) or (not password[li] == char and password[ri] == char)
