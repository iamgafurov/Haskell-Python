mysqrt :: (Num a,Fractional a,Ord a) => a->a
mysqrt x = mysqrtAcc (1+x) x

mysqrtAcc :: (Num a,Fractional a,Ord a) => a->a->a
mysqrtAcc x a
      | abs (xn-x) < 1e-15 = xn
      |  otherwise = mysqrtAcc xn a
       where xn = (x+a/x)/2

mySin :: (Num a,Fractional a,Ord a) => a->a
mySin a = mySinAcc 0 a 1 a

mySinAcc ::(Num a,Fractional a,Ord a) => a->a->a->a->a
mySinAcc s a n x
   | abs a < 1e-15 = s
   | otherwise = mySinAcc (s+a) ( ((-a) * x*x )/((n+1)*(n+2))) (n+2) x
  
gett a = ((:)t a)