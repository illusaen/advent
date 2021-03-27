import utils

def main():
  content = utils.readFile('../../inputs/day7.txt')
  print("Shiny gold bag can go into " + str(len(utils.findElements(content, "shiny gold"))) + " bags.")

  content = utils.readFile('../../inputs/day7.txt')
  print("Shiny gold bag must contain " + str(utils.findNumberOfBags(content, "shiny gold")) + " bags.")

if __name__ == "__main__":
  main()
