import utils

def main():
  content = utils.readFile('../../inputs/day5-sample.txt')
  print("Highest seat ID is " + str(utils.findElements(content)) + ".")

if __name__ == "__main__":
  main()
