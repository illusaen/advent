import re

def readFile(name):
  with open(name, 'r') as f:
    content = [line.rstrip() for line in f.readlines() if re.compile(r'[FB]{7}[LR]{3}').match(line) is not None]
  return content

def findElements(binary):
  print(binary)
  return 0
