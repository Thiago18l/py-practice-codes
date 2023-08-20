def exponential(n: int) -> list:
    aux: list = []
    result: list = []
    for i in range(n):
        if i < n:
            aux.append(i)
    
    for i in aux:
        result.append(int(i**2))
    return result
