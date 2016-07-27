

doubleSum :: [Integer] -> Integer
doubleSum [] = 0
doubleSum xs = foldr (+) (foldr (+) 0 xs) xs

sumList :: [Integer] -> Integer
sumList xx = aux xx 0
    where
        aux [] n     = n
        aux (x:xs) n = aux xs (n + x)

data DecTree = Branch (Bool) (DecTree) (DecTree)
             | Leaf Integer

three :: DecTree
three = Branch (True)
    (Branch (False) (Branch (True) (Leaf 1) (Leaf 2)) (Branch (False) (Leaf 3) (Leaf 4)))
    (Branch (True) (Branch (True) (Leaf 5) (Leaf 6)) (Branch (False) (Leaf 7) (Leaf 8)))

decide :: DecTree -> Integer
decide (Branch condition left right)
            | condition = decide left
            | otherwise = decide right
decide (Leaf i) = i

fook :: Integer -> (Integer -> a) -> a
fook n k = k (n * 2)

fooPairk :: (Integer, Integer) -> (Integer -> a) -> (a, a)
fooPairk (a,b) k = (fook a k, fook b k)

foo :: (Integer, Integer) -> Integer
foo p@(f, s) = fst p
