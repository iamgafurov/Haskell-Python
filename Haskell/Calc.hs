------------------------------------------------------------
-- Expression Calculator
------------------------------------------------------------
module Calc (
    Lexeme(..),
    Value(..),
    spanLex,
    lexemes,
    evaluate
) where

import Data.Char

------------------------
-- Work with triples
------------------------
first :: (a, b, c)->a
first (x, _, _) = x

second :: (a, b, c)->b
second (_, y, _) = y

third :: (a, b, c)->c
third (_, _, z) = z

------------------------------------------------
-- Types of tokens
------------------------------------------------
data Lexeme = Number | LPar | RPar | 
              Plus | Minus | Mult | Div |
              Name | Empty | Illegal
              deriving (Eq, Show)

--------------------------------------------------------------------
-- Extract the first lexeme from the string
-- Return a pair:
-- ((lex. type, lex. value, lex. text), a rest of the string)
-- (the first component of pair is a triple that describes a lexeme)
--------------------------------------------------------------------
spanLex :: String->((Lexeme, Double, String), String)
spanLex str = spanLex' ("", Empty) str

spanLex' :: (String, Lexeme)->String->
            ((Lexeme, Double, String), String)
spanLex' (lexText, lex) []
    | lex == Number  = ((Number, read lexText::Double, lexText), [])
    | otherwise      = ((lex, 0.0, ""), [])
spanLex' (lexText, lex) str@(h:t)
    | lex == Empty =
      if isNumber h then spanLex' ([h], Number) t
      else if isAlpha h then spanLex' ([h], Name) t
      else if h == '(' then ((LPar, 0.0, [h]), t)
      else if h == ')' then ((RPar, 0.0, [h]), t)
      else if h == '+' then ((Plus, 0.0, [h]), t)
      else if h == '-' then ((Minus, 0.0, [h]), t)
      else if h == '*' then ((Mult, 0.0, [h]), t)
      else if h == '/' then ((Div, 0.0, [h]), t)
      else if isSpace h then spanLex' (lexText, lex) t    -- Ignore space
      else ((Illegal, 0.0, [h]), t)
    | lex == Number =
      let (digits, rest) = span (\ x -> isDigit x || x == '.') str
          txt = lexText ++ digits
          value = read (txt)::Double
      in ((Number, value, txt), rest)
    | lex == Name =
      let (letters, rest) = span isAlphaNum str
          txt = lexText ++ letters
      in ((Name, 0.0, txt), rest)
    | otherwise = error "spanLex error"

------------------------------------------------
-- Split a string into a list of lexemes
------------------------------------------------
lexemes :: String->[(Lexeme, Double, String)]
lexemes str = lexemes' [] str

lexemes' :: [(Lexeme, Double, String)]->String->
            [(Lexeme, Double, String)]
lexemes' acc [] = acc
lexemes' acc str =
    let (token, rest) = spanLex str
    in lexemes' (acc ++ [token]) rest

---------------------------------------------------------------
-- Value calculated by the Calculaor:
-- It may be some error or a correct Double value.
-- In case of error (syntax etc.) we present a text String
--     with the explanation of error.
-- So, a Value is represented by a triple: Bool, Double, String
---------------------------------------------------------------
data Value = Value {
    correct :: Bool,
    number :: Double,
    errorText :: String
} deriving (Show)

correctValue :: Double->Value
correctValue x = (Value True x "")

errorValue :: String->Value
errorValue txt = (Value False 0 txt)

---------------------------------------------------------------

-- Context Free Grammar for Expressions
-- F -> T | F + T | F - T
-- T -> M | T * M | T / M
-- M -> n | ( F ) | -M | name ( F )
--
-- Transform into a left-recursive form:
-- F -> T F'
-- F' -> eps | + T F' | - T F'
-- T -> M T'
-- T' -> eps | * M T' | / M T'
-- M -> n | ( F ) | -M  | name ( F )
----------------------------------------
evaluate :: String->Value
evaluate str =
    let 
        tokens = lexemes str
        (value, rest) = valueF tokens
        restNonempty = (length rest) >= 2 || 
                       (rest /= [] && first (head rest) /= Empty)
    in 
        if (not (correct value)) then
            value
        else if restNonempty then
            errorValue "Syntax error: Incorrect end of formula"
        else 
            value

valueF :: [(Lexeme, Double, String)]->
          (Value, [(Lexeme, Double, String)])
valueF tokens =
     let (t, rest) = valueT tokens
     in
         if not (correct t) then
             (t, rest)
         else 
             valueF' t rest

valueF' :: Value->[(Lexeme, Double, String)]->
           (Value, [(Lexeme, Double, String)])
valueF' acc ((Plus, _, _):tokens) =
     let (t, rest) = valueT tokens
     in 
         if not (correct t) then
             (t, tokens)
         else 
             valueF' (correctValue (number acc + number t)) rest
valueF' acc ((Minus, _, _):tokens) =
     let (t, rest) = valueT tokens
     in
         if not (correct t) then
             (t, tokens)
         else 
             valueF' (correctValue (number acc - number t)) rest
valueF' acc tokens = (acc, tokens)

valueT :: [(Lexeme, Double, String)]->
          (Value, [(Lexeme, Double, String)])
valueT tokens =
     let (m, rest) = valueM tokens
     in
         if not (correct m) then
             (m, tokens)
         else 
             valueT' m rest

valueT' :: Value->[(Lexeme, Double, String)]->
           (Value, [(Lexeme, Double, String)])
valueT' acc ((Mult, _, _):tokens) =
     let (m, rest) = valueM tokens
     in
         if not (correct m) then
             (m, tokens)
         else 
             valueT' (correctValue (number acc * number m)) rest
valueT' acc ((Div, _, _):tokens) =
     let (m, rest) = valueM tokens
     in --valueT' (acc/m) rest
         if not (correct m) then
             (m, tokens)
         else 
             valueT' (correctValue (number acc / number m)) rest
valueT' acc tokens = (acc, tokens)

valueM :: [(Lexeme, Double, String)]->
          (Value, [(Lexeme, Double, String)])
valueM ((Number, num, _):rest) = ((Value True num ""), rest)
valueM ((LPar, _, _):tokens) =
    let 
        (f, rest) = valueF tokens
        errorSyntax = (rest == [] || first (head rest) /= RPar)
    in
        if errorSyntax then
            (errorValue "Syntax error: no )", rest)
        else 
            (f, tail rest)
valueM ((Minus, _, _):tokens) =
    let 
        (m, rest) = valueM tokens
    in
        (correctValue (-number m), rest)
valueM ((Name, _, txt):(LPar, _, _):tokens) =
    let 
        (f, rest) = valueF tokens
        m = if (rest == [] || first (head rest) /= RPar)
            then errorValue "Syntax error in function call"
            else if txt == "sin" then correctValue (sin (number f))
            else if txt == "cos" then correctValue (cos (number f))
            else if txt == "exp" then correctValue (exp (number f))
            else if txt == "log" then correctValue (log (number f))
            else if txt == "sqrt" then correctValue (sqrt (number f))
            else if txt == "atan" then correctValue (atan (number f))
            else errorValue ("Error: Unknown function " ++ txt)
    in
        (m, tail rest)
valueM tokens = ((errorValue "Syntax error"), tokens)
