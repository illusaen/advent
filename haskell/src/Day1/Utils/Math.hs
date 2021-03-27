module Day1.Utils.Math (combinations, findSequence) where

combinations :: Int -> [a] -> [[a]]
combinations n arr
  | n == 0 = [[]]
  | null arr = []
  | otherwise = map (x:) (combinations (n-1) xs) ++ combinations n xs
    where (x:xs) = arr

findSequence :: Int -> [[Int]] -> [([Int], Int)]
findSequence desired arr = [ (seq, product seq) | seq <- arr, sum seq == desired ]
