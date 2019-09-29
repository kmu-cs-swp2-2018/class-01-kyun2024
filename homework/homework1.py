import time

def fibo(nbr):
    if(nbr <= 1):
        return 1
    return fibo(nbr-1)+fibo(nbr-2)

def iterfibo(nbr):
    n_0 = 1
    n_1 = 1
    n_2 = 1
    for i in range(2,nbr+1):
        n_2 = n_0 + n_1
        n_0 = n_1
        n_1 = n_2
    return n_2

while True:
    nbr = int(input("Enter a number: "))
    if nbr == -1:
        break
    ts = time.time()
    fibonumber = iterfibo(nbr)
    ts = time.time() - ts
    print("IterFibo(%d)=%d, time %.6f" %(nbr, fibonumber, ts))
    ts = time.time()
    fibonumber = fibo(nbr)
    ts = time.time() - ts
    print("Fibo(%d)=%d, time %.6f" %(nbr, fibonumber, ts))