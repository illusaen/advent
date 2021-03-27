# ###
# Note: Since we're not running as package, must have:
#   import sys
#   from os import path
#   sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
# above the import of this file.
# ###

def prettyPrint2D(matrix, sep=" "):
  print("\n".join(sep.join([str(cell) for cell in row]) for row in matrix) + "\n")

def flatten(array2D):
  return (item for sublist in array2D for item in sublist)
