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
validate (InputLine min' max' char password)
  | min' == 0 || char == "" = True
  | null password = False
  | otherwise = min' <= occurences && (max' == -1 || max' >= occurences)
  where
    occurences = length $ filter (\c -> char == "" || head char == c) password

validatePart2 :: InputLine -> Bool
validatePart2 (InputLine min' max' char password)
  | char == "" = True
  | li < 0 || ri < 0 || null password = False
  | otherwise = (password !! li == head char && password !! ri /= head char) || (password !! li /= head char && password !! ri == head char)
  where
    li = min' - 1
    ri = max' - 1

contents :: IO [InputLine]
contents = do
  c <- readFile "../inputs/day2.txt"
  return $ filter validatePart2 (map (parseInput . words) (lines c))
