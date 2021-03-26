from argparse import ArgumentParser
import utils

def parseArgs():
  parser = ArgumentParser(description='Process arguments.')
  parser.add_argument('sum', metavar='S', type=int, help='sum to match')
  parser.add_argument('number', metavar='N', type=int, help='number of elements that sum up to the given sum')
  return parser.parse_args()

def main():
  args = parseArgs()
  content = utils.readFile('../../inputs/day1.txt')

  els = utils.findElements(content, args.sum, args.number)
  print("\n".join([ "Found [" + ", ".join([str(ie) for ie in e]) + "] with product of " + str(p) + "." for e, p in els ]))

if __name__ == "__main__":
  main()
