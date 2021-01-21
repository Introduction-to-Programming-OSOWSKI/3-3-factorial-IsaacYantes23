def factorial(y):
    
    number = 1
   
    for i in range(1, y + 1):
        number = number * i
        
    return number

print(factorial(5))
