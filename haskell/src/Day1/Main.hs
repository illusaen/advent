module Day1.Main (main) where

import Options.Applicative
import Data.Semigroup ((<>))

import Day1.Utils.IO (contents, output)
import Day1.Utils.Math (combinations, findSequence)

data Options = Options { optionSum :: String, optionNumber :: String }

parseOptions :: Parser Options
parseOptions = Options
  <$> argument str (metavar "SUM")
  <*> argument str (metavar "NUMBER")

run :: Options -> IO ()
run opts = do
      c <- contents
      output . findSequence (read (optionSum opts) :: Int) $ combinations (read (optionNumber opts) :: Int) c

main = run =<< execParser opts
  where
    opts = info (parseOptions <**> helper) 
      ( fullDesc
      <> progDesc "Gets the products of sequences of LENGTH numbers summing up to SUM"
      <> header "Advent of code" )