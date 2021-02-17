cube = lambda x: x ** 3


def fibonacci(n):
    L = [0, 1]
    for i in range(2, n):
        L.append(L[i-1] + L[i-2])
        
    return(L[0:n])

if _name_ == '_main_':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
