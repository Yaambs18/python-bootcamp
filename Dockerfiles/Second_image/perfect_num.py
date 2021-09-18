def perfect_num(num):
    sum = 0
    for i in range(1,num):
        if num%i==0:
            sum+=i
    if sum==num:
        return f"The {num} is perfect number."
    
    return f"The {num} is not a perfect number."
    
n = int(input("Enter a number :"))
print(perfect_num(n))
