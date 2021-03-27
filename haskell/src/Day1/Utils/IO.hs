module Day1.Utils.IO (contents, output) where

import Data.Maybe (mapMaybe)
import Text.Read (readMaybe)
import Data.List (intercalate)
import Data.Tuple (fst, snd)

contents :: IO [Int]
contents = do
    contents <- readFile "../inputs/day1.txt"
    return $ mapMaybe (readMaybe :: String -> Maybe Int) (lines contents)

formatted :: ([Int], Int) -> String
formatted tuple = unwords [ "Found", "[" ++ intercalate ", " (map show $ fst tuple) ++ "]", "with product of", show (snd tuple) ++ "." ]

output :: [([Int], Int)] -> IO ()
output arr
    | null arr = putStrLn "No sequences found."
    | otherwise = mapM_ (putStrLn . formatted) arr
