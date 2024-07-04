\ LP format - for model browsing. Use MPS format to capture full model detail.
Minimize
  - 10 delivery[Monday] - 30 delivery[Tuesday] - 50 delivery[Wednesday]
   - 90 delivery[Thursday] - 180 delivery[Friday] - 100 delivery[Saturday]
   - 60 delivery[Sunday] + 300 trucks[Monday] + 300 trucks[Tuesday]
   + 300 trucks[Wednesday] + 300 trucks[Thursday] + 300 trucks[Friday]
   + 300 trucks[Saturday] + 300 trucks[Sunday] + 72000 Constant + [
   0.4 delivery[Monday] ^2 + 0.4 delivery[Tuesday] ^2
   + 0.4 delivery[Wednesday] ^2 + 0.4 delivery[Thursday] ^2
   + 0.4 delivery[Friday] ^2 + 0.4 delivery[Saturday] ^2
   + 0.4 delivery[Sunday] ^2 ] / 2 
Subject To
 R0: delivery[Monday] + delivery[Tuesday] + delivery[Wednesday]
   + delivery[Thursday] + delivery[Friday] + delivery[Saturday]
   + delivery[Sunday] = 1300
 R1: delivery[Monday] - 100 trucks[Monday] <= 0
 R2: delivery[Tuesday] - 100 trucks[Tuesday] <= 0
 R3: delivery[Wednesday] - 100 trucks[Wednesday] <= 0
 R4: delivery[Thursday] - 100 trucks[Thursday] <= 0
 R5: delivery[Friday] - 100 trucks[Friday] <= 0
 R6: delivery[Saturday] - 100 trucks[Saturday] <= 0
 R7: delivery[Sunday] - 100 trucks[Sunday] <= 0
Bounds
 Constant = 1
Generals
 delivery[Monday] delivery[Tuesday] delivery[Wednesday] delivery[Thursday]
 delivery[Friday] delivery[Saturday] delivery[Sunday] trucks[Monday]
 trucks[Tuesday] trucks[Wednesday] trucks[Thursday] trucks[Friday]
 trucks[Saturday] trucks[Sunday]
End
