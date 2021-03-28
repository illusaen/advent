import utils

def main():
  content = utils.readFile('../../inputs/day9.txt')

  total = utils.findElements(content, 25, 25)
  print("First invalid input is %d." % total)
  print("Encryption weakness is %d." % utils.findSequence(content, total))

if __name__ == "__main__":
  main()
