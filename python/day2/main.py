import utils

def main():
  content = utils.readFile('../../inputs/day2.txt')

  els = utils.findElements(content)
  if len(els) == 0:
    print("No sequences found.")
  else:
    print("Found " + str(len(els)) + " entries.")

if __name__ == "__main__":
  main()
