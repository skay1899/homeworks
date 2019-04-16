#Contents of file fib.py
#function to generate fibonacci series given 'n'

def fib(n):
	ar = [0,1]
	while len(ar) < n+1:
		ar.append(0)
	if n <= 1:  
        return n  
    else:  
        if ar[n - 1] == 0:  
            ar[n - 1] = fibonacci(n - 1)  
  
        if ar[n - 2] == 0:  
            ar[n - 2] = fibonacci(n - 2)  
              
    ar[n] = ar[n - 2] + ar[n - 1]  
    return ar[n]
