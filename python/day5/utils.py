import re

def readFile(name):
  with open(name, 'r') as f:
    content = [line.rstrip() for line in f.readlines() if re.compile(r'[FB]{7}[LR]{3}').match(line) is not None]
  return content

def binarySplit(str, minV, maxV):
  if minV == maxV or maxV == 0 or len(str) == 0:
    return maxV
  
  isLower = str[0] in ["F", "L"]
  halved = (minV + maxV) // 2
  return binarySplit(str[1:], minV if isLower else halved + 1, halved if isLower else maxV)

def split(str, total):
  return binarySplit(str, 0, total - 1)

def findElements(binary, rows, columns):
  seatIds = [split(b[:7], rows) * columns + split(b[7:], columns) for b in binary]
  emptySeatIds = set(range(0, max(seatIds) + 1)) - set(seatIds)
  nonConsecutiveEmptySeatIds = [s for s in emptySeatIds if s - 1 not in emptySeatIds and s + 1 not in emptySeatIds]
  return nonConsecutiveEmptySeatIds[0] if len(nonConsecutiveEmptySeatIds) > 0 else -1
