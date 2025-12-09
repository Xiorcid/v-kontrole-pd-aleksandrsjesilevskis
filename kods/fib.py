fib = []
fib.append(0)
fib.append(1)

for i in range(1,99):
    fib.append(fib[i]+fib[i-1])
    
for n in range(99, -1, -1):
    print(fib[n])
