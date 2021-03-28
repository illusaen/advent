from itertools import combinations

def readFile(name):
  with open(name, 'r') as f:
    content = [int(line) for line in f.readlines()]
  return content

def nextDevice(hashed, differences, currentJoltage, maxJump):
  if currentJoltage >= len(hashed):
    return
  
  for indices in range(currentJoltage + 1, currentJoltage + maxJump + 1):
    if hashed[indices]:
      diff = indices - currentJoltage
      differences[diff] += 1
      current = indices
      break
  
  if current == currentJoltage:
    return

  return nextDevice(hashed, differences, current, maxJump)

def setup(contents, deviceDifference, maxJump):
  deviceJoltage = max(contents) + deviceDifference
  hashed = { i:0 for i in range(1, deviceJoltage + 1) }
  differences = { i:0 for i in range(1, maxJump + 1) }
  for i in contents:
    hashed[i] += 1
  hashed[deviceJoltage] = 1

  return hashed, differences

def findDifferences(contents, maxJump, deviceDifference, outletJoltage = 0):
  hashed, differences = setup(contents, deviceDifference, maxJump)
  nextDevice(hashed, differences, outletJoltage, maxJump)

  return differences[1] * differences[3]

def findCombinations(contents, maxJump, deviceDifference, outletJoltage = 0):
  hashed, _ = setup(contents, deviceDifference, maxJump)
  


  return 1
