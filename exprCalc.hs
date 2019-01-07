import Calc

main = do
    putStrLn "\nEnter an expression:"
    line <- getLine      
    if null line || line == "quit"
    then return ()
    else do
        let res = evaluate line
            txt = if (correct res)
                  then "= " ++ (show (number res))
                  else (errorText res)
        putStrLn txt
        main
