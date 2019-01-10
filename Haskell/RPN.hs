
calc lst = (calcAcc (words lst) [])
calcAcc lst acc
    | lst == []           = head acc
    | head lst == "+"     = calcAcc (tail lst)  (head(acc) + head(tail acc):tail(tail acc))
    | head lst == "-"     = calcAcc(tail lst)  (head(acc) - head(tail acc):tail(tail acc))
    | head lst == "*"     = calcAcc(tail lst)  (head(acc)*head(tail acc):tail(tail acc))
    | head lst == "/"     = calcAcc(tail lst)  (head(acc)/head(tail acc):tail(tail acc))
    | head lst == "sin"     = calcAcc(tail lst)  ((sin (head acc)):(tail acc))
    | head lst == "cos"     = calcAcc(tail lst)  ((cos (head acc)):(tail acc))
    | otherwise            = calcAcc(tail lst)  ((read (head lst)::Double):acc)
