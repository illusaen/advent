import utils

def main():
  content = utils.readFile('../../inputs/day10.txt')
  print("Device joltage difference product is %d." % utils.findDifferences(content, 3, 3))
  print("Number of combinations of adapters is %d." % utils.findCombinations(content, 3, 3))

if __name__ == "__main__":
  main()
