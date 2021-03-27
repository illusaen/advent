import utils

def main():
  content = utils.readFile('../../inputs/day4.txt')
  print("Found " + str(utils.findElements(content, ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'], ['cid'])) + " valid passports.")

if __name__ == "__main__":
  main()
