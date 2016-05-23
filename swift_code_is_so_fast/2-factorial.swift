func factorial(N: Int) -> (Int)
{
    if N == 1 || N == 0{
        return 1
    }
    else{
        return N * factorial(N-1)
    }
}
