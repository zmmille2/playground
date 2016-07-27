factk :: Integer -> (Integer -> a) -> a
factk 0 k = k 1
factk n k = factk (n - 1) (\a -> k (n * a))
