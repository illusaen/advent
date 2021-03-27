def readFile(name):
  with open(name, 'r') as f:
    content = f.read().rstrip().split('\n\n')
  return content

def findUniqueElements(contents):
  return [len(set(group.rstrip().replace('\n', ''))) for group in contents]

def findMatchedElements(contents):
  return [len(set.intersection(*[set(x) for x in group.rstrip().split('\n')])) for group in contents]
