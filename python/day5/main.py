import utils

def main():
  content = utils.readFile('../../inputs/day5.txt')
  print("Highest seat ID is " + str(utils.findElements(content, 128, 8)) + ".")

if __name__ == "__main__":
  main()
