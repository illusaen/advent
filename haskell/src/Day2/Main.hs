module Day2.Main (main) where

import Day2.IO (contents)

main = do
  c <- contents
  print $ unwords [ "Found", show (length c), "valid entries." ]
