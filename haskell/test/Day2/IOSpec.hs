module Day2.IOSpec (spec) where

import SpecHelper
import Day2.IO

spec :: Spec
spec = do
  describe "parseInput" $ do
    context "when provided with zero cases" $ do
      it "should have 0 min if input has no min" $
        parseInput ["-2", "a:", "asdf"] `shouldBe` InputLine { min'=0, max'=2, char="a", password="asdf" }
      it "should have 0 min if input min is non decimal" $
        parseInput ["a-2", "a:", "asdf"] `shouldBe` InputLine { min'=0, max'=2, char="a", password="asdf" }
      it "should have -1 max if input has no max" $
        parseInput ["2-", "a:", "asdf"] `shouldBe` InputLine { min'=2, max' = -1, char="a", password="asdf" }
      it "should have -1 max if input has no max" $
        parseInput ["2-a", "a:", "asdf"] `shouldBe` InputLine { min'=2, max' = -1, char="a", password="asdf" }
      it "should get correct char if no semicolon at end of char" $
        parseInput ["2-4", "a", "asdf"] `shouldBe` InputLine { min'=2, max' = 4, char="a", password="asdf" }
    context "when provided with [\"50-100\", \"b:\", \"asdf\"]" $ do
      it "should parse correctly" $
        parseInput ["50-100", "b:", "asdf"] `shouldBe` InputLine { min'=50, max'=100, char="b", password="asdf" }

  describe "validate" $ do
    context "when provided with zero cases" $ do
      it "should return true if 0 min" $
        validate InputLine { min'=0, max' = 4, char="a:", password="asdf" } `shouldBe` True
      it "should return true if char is empty" $
        validate InputLine { min'=1, max' = 4, char="", password="asdf" } `shouldBe` True
      it "should return false if password is empty" $
        validate InputLine { min'=1, max' = 4, char="a:", password="" } `shouldBe` False
    context "when provided with good data" $ do
      it "should return true when using 1/2/a/asdf" $
        validate InputLine { min'=1, max' = 2, char="a:", password="asdf" } `shouldBe` True
      it "should return true when using 1/2/a/aasdf" $
        validate InputLine { min'=1, max' = 2, char="a:", password="aasdf" } `shouldBe` True
      it "should return false when using 1/2/a/aasdfa" $
        validate InputLine { min'=1, max' = 2, char="a:", password="aasdfa" } `shouldBe` False
  
  describe "validatePart2" $ do
    context "when provided with zero cases" $ do
      it "should return true if char is empty" $
        validatePart2 InputLine { min'=1, max' = 4, char="", password="asdf" } `shouldBe` True
      it "should return false if password is empty" $
        validatePart2 InputLine { min'=1, max' = 4, char="a:", password="" } `shouldBe` False
      it "should return false if min is 0" $
        validatePart2 InputLine { min'=0, max' = 4, char="a:", password="asdf" } `shouldBe` False
      it "should return false if max is 0" $
        validatePart2 InputLine { min'=1, max' = 0, char="a:", password="asdf" } `shouldBe` False
    context "when provided with good data" $ do
      it "should return true when 1-based index min matches char and 1-based index max doesn't" $
        validatePart2 InputLine { min'=1, max' = 2, char="a:", password="asdf" } `shouldBe` True
      it "should return true when 1-based index min doesn't match char and 1-based index max does" $
        validatePart2 InputLine { min'=1, max' = 2, char="a:", password="sadf" } `shouldBe` True
      it "should return false when both 1-based index min and 1-based index max both match char" $
        validatePart2 InputLine { min'=1, max' = 2, char="a:", password="aasdf" } `shouldBe` False
      it "should return false when neither 1-based index min nor 1-based index max match char" $
        validatePart2 InputLine { min'=1, max' = 2, char="a:", password="fghi" } `shouldBe` False