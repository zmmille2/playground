data Stack a = Empty | Node a (Stack a) deriving (Show)

peek :: Stack a -> (Maybe a)
peek Empty       = Nothing
peek (Node a _ ) = (Just a)

push :: a -> Stack a -> Stack a
push node stack = (Node node (stack))

pop :: Stack a -> (Maybe a, Stack a)
pop Empty        = (Nothing, Empty)
pop (Node n (s)) = (Just n, s)
