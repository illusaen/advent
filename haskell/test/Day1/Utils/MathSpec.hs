module Day1.Utils.MathSpec (spec) where

import SpecHelper
import Day1.Utils.Math

spec :: Spec
spec = do
  describe "combinations" $ do
    context "when provided with zero cases" $ do
      it "should be empty if length is 0" $
        combinations 0 [1..10] `shouldBe` [[]]
      it "should be empty if list is empty" $
        combinations 2 ([] :: [Int]) `shouldBe` []
      it "should be empty if length is greater than list length" $
        combinations 4 [1..3] `shouldMatchList` []
    context "when provided with [1..3]" $ do
      it "should return appropriate sequences if length is 2" $
        combinations 2 [1..3] `shouldMatchList` [ [1, 2], [2, 3], [1, 3] ]
      it "should return appropriate sequences if length is 3" $
        combinations 3 [1..3] `shouldMatchList` [ [1, 2, 3] ]
  describe "findSequence" $ do
    context "when provided with zero cases" $ do
      it "should be empty if list is empty" $
        findSequence 5 ([[]] :: [[Int]]) `shouldBe` []
      it "should be empty if list does not contain sequence with that sum" $
        findSequence 6 [[1, 2], [1, 3], [2, 3]] `shouldBe` []
    context "when provided with [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]" $ do
      it "should show all relevant sequences and their products" $
        findSequence 5 [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]] `shouldMatchList` [ ([1, 4], 4), ([2, 3], 6) ]