import re

BAG_NAME_CONTAINS_DELIM = ' bags contain '
def parsed(line):
  split = line.split(BAG_NAME_CONTAINS_DELIM)
  containees = {} if split[1] == 'no other bags.' else {y:int(x) for x, y, _ in re.compile(r'(\d+) ([a-z ]+?) bags?(, |\.)').findall(split[1])}
  return [split[0], containees]

def readFile(name):
  with open(name, 'r') as f:
    content = dict(parsed(line) for line in f.readlines() if BAG_NAME_CONTAINS_DELIM in line)
  return content

def findDirectContainersOf(contents, bagName):
  return set([bagK for bagK, bagC in contents.items() if bagName in bagC.keys() and bagC[bagName] > 0])

def findElements(contents, bagName, total = set()):
  directContainers = findDirectContainersOf(contents, bagName)
  total |= directContainers
  for container in directContainers:
    findElements(contents, container, total)

  return total

def findNumberOfBags(contents, bagName):
  if not bagName in contents.keys() or len(contents[bagName]) == 0:
    return 0
  
  return sum([ childBagNumber * (findNumberOfBags(contents, childBagName) + 1) for childBagName, childBagNumber in contents[bagName].items() ])
