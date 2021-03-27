import utils

def main():
  content = utils.readFile('../../inputs/day6.txt')
  print("Sum of all groups' unique counts: " + str(sum(utils.findUniqueElements(content))) + ".")
  print("Sum of all groups' matched counts: " + str(sum(utils.findMatchedElements(content))) + ".")

if __name__ == "__main__":
  main()
