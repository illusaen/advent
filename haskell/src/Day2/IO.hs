module Day2.IO where

import Data.List.Split (splitOn)
import Data.Maybe (fromMaybe)
import Text.Read (readMaybe)

data InputLine = InputLine { min' :: Int, max' :: Int, char :: String, password :: String } deriving (Eq, Show)

parseInput :: [String] -> InputLine
parseInput str = InputLine {
  min' = fromMaybe 0 (readMaybe minString :: Maybe Int),
  max' = fromMaybe (-1) (readMaybe maxString :: Maybe Int),
  char = take 1 b,
  password = password }
  where
    (a:b:password:_) = str
    (minString:maxString:_) = splitOn "-" a

validate :: InputLine -> Bool
validate input
  | minOccurrences == 0 || ch == "" = True
  | null pwd = False
  | otherwise = minOccurrences <= occurences && (maxOccurrences == -1 || maxOccurrences >= occurences)
  where
    occurences = length $ filter (\c -> ch == "" || head ch == c) pwd
    minOccurrences = min' input
    maxOccurrences = max' input
    pwd = password input
    ch = char input

validatePart2 :: InputLine -> Bool
validatePart2 input
  | ch == "" = True
  | li < 0 || ri < 0 || null pwd = False
  | otherwise = (pwd !! li == head ch && pwd !! ri /= head ch) || (pwd !! li /= head ch && pwd !! ri == head ch)
  where
    li = min' input - 1
    ri = max' input - 1
    pwd = password input
    ch = char input

contents :: IO [InputLine]
contents = do
  c <- readFile "../inputs/day2.txt"
  return $ filter validatePart2 (map (parseInput . words) (lines c))
