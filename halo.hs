divisors  n = [ d | d<- [1..n], (mod n d) == 0 ]

divisible n lst
    | lst == []                 = False
    | mod n (head lst) == 0     = True
    | otherwise                 = divisible n (tail lst)
    
mult n lst
    | lst == [] = []
    | n==1 = []
    | head lst ==1 =   mult n (tail lst) 
    | mod n (head lst ) == 0 =  head lst :  mult (div n (head lst)) lst
    | otherwise  =  mult n (tail lst)

multiplicatives  n = mult n (divisors  n)

perfect n =sum(init (divisors  n)) ==n

semiperfect n  = partialsum (init(divisors n)) n

partialsum lst n
    | lst == [] = n==0
    | otherwise  = partialsum (tail lst) (n- head lst) || partialsum (tail lst) n