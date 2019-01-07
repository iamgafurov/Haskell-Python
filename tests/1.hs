last [x] = x
last (_:xs)   = last xs

fst (x,_) = x

init [x] = []
init (x:xs) = x : init x

power : Int->Int->Int
power x 0 = 1
power x y = x* power x (y-1)
