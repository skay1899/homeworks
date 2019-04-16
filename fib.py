#Contents of file fib.py
#function to generate fibonacci series given 'n'

def fib(n):
	ar = [0,1]
	while len(ar) < n+1:
		ar.append(0)
	if n <= 1:  
        return n  
    else:  
        if FibArray[n - 1] == 0:  
            FibArray[n - 1] = fibonacci(n - 1)  
  
        if FibArray[n - 2] == 0:  
            FibArray[n - 2] = fibonacci(n - 2)  
              
    FibArray[n] = FibArray[n - 2] + FibArray[n - 1]  
    return FibArray[n]
