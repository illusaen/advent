from itertools import combinations

def readFile(name):
  with open(name, 'r') as f:
    content = [int(line) for line in f.readlines()]
  return content

def findElements(contents, preamble, saved):
  for i in range(preamble, len(contents)):
    sums = [comb for comb in combinations(contents[i-saved:i], 2) if sum(comb) == contents[i]]
    if not len(sums):
      return contents[i]
  
  return -1

def findSequence(contents, total):
  for i in range(len(contents) - 1):
    for j in range(i + 1, len(contents)):
      c = contents[i:j]
      if sum(c) == total:
        return min(c) + max(c)
  return -1