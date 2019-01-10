lstToN lst = lton 0 lst
lton  acc lst 
     | lst ==[] = acc
     | otherwise = lton(acc * 10 + (head lst)) (tail lst)
     

     
ntoLst n = ntol n []
ntol acc lst
    | acc== 0 = lst
    | otherwise = ntol (acc `div` 10)  ((acc `mod` 10): lst)
    

    
    
multbytwo lst = ntoLst ((lstToN lst)*2)