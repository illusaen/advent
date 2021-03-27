import utils

def main():
  content = utils.readFile('../../inputs/day3.txt')
  print("Found " + str(utils.findTotalElements(content, [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)])) + " trees.")

if __name__ == "__main__":
  main()
