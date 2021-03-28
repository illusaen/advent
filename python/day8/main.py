import utils

def main():
  content = utils.readFile('../../inputs/day8.txt')
  print("About to repeat index %d with acc %d." % utils.findElements(content))

  content = utils.readFile('../../inputs/day8.txt')
  print("Fixing index %d with acc %d." % utils.findCorruptedElement(content))

if __name__ == "__main__":
  main()
