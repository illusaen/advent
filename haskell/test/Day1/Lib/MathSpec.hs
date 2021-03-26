module Day1.Lib.MathSpec (spec) where

import SpecHelper
import Day1.Lib.Math

spec :: Spec
spec = do
  describe "sumGs" $ do
    context "with [1..10]" $
      it "should be 55" $
        sumG 1 10 `shouldBe` 55
