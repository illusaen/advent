import re
from collections import namedtuple
from copy import deepcopy

Instruction = namedtuple('Instruction', ['cmd', 'arg'])
VALID_COMMANDS = {'ACCUMULATE': 'acc', 'JUMP': 'jmp', 'NOP': 'nop'}

def readFile(name):
  p = re.compile('(%s) ((\+|\-)\d+)' % "|".join(VALID_COMMANDS.values()))
  with open(name, 'r') as f:
    content = [Instruction(cmd, int(arg)) for line in f.readlines() for cmd, arg, _ in p.findall(line)]
  return content

def nextIndex(instruction):
  return instruction.arg if instruction.cmd == VALID_COMMANDS['JUMP'] else 1

def findElements(contents):
  acc = 0
  index = 0
  visitedIndices = []
  while index < len(contents) and index + nextIndex(contents[index]) not in visitedIndices:
    visitedIndices.append(index)
    instruction = contents[index]
    index += nextIndex(instruction)
    acc += instruction.arg if instruction.cmd == VALID_COMMANDS['ACCUMULATE'] else 0
  return (index, acc)

def findCorruptedElement(contents):
  for instructionIndex, instruction in enumerate(contents):
    if instruction.cmd not in [VALID_COMMANDS['JUMP'], VALID_COMMANDS['NOP']]:
      continue

    newInstructionList = deepcopy(contents)
    newInstructionList[instructionIndex] = Instruction(VALID_COMMANDS['NOP'] if instruction.cmd == VALID_COMMANDS['JUMP'] else VALID_COMMANDS['JUMP'], instruction.arg)

    index, acc = findElements(newInstructionList)
    if index == len(newInstructionList):
      return (instructionIndex, acc)

  return (-1, -1)
