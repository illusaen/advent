import re

def toPassport(fieldList):
  return {x:y for f in fieldList for x, y in [f.split(":")] if ":" in f}

def readFile(name):
  with open(name, 'r') as f:
    content = [toPassport(p.replace('\n', ' ').replace('  ', ' ').split(' ')) for p in f.read().rstrip().split('\n\n')]
  return content

def fieldValid(field, value):
  def validateYear(minValue, maxValue):
    y = int(value) or 0
    return len(value) == 4 and minValue <= y and y <= maxValue
  
  def validateHeight():
    unit = value[-2:]
    if len(value) <= 2 or (unit != 'cm' and unit != 'in'):
      return False
    h = int(value[:-2]) or 0
    return (unit == 'cm' and 150 <= h and h <= 193) or (unit == 'in' and 59 <= h and h <= 76)

  switcher = {
    'byr': lambda: validateYear(1920, 2002),
    'iyr': lambda: validateYear(2010, 2020),
    'eyr': lambda: validateYear(2020, 2030),
    'hgt': validateHeight,
    'hcl': lambda: re.compile(r'^#[0-9a-f]{6}$').match(value) is not None,
    'ecl': lambda: value in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'],
    'pid': lambda: len(value) == 9 and int(value)
  }

  return switcher.get(field, lambda: False)()

def valid(passport, required, optional):
  return all(elem in passport.keys() and fieldValid(elem, passport[elem]) for elem in required)

def findElements(passports, required, optional):
  return len([passport for passport in passports if valid(passport, required, optional)])
