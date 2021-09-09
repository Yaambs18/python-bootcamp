# Write a function called myfunc that prints the string 'Hello World'
def myfunc():
    print('Hello World')
myfunc()

# Write a function called myfunc that takes in name and prints 'Hello Name'
def myfunc():
    name = input("Enter your name: ")
    print('Hello {}'.format(name))
myfunc()

# Write a function called myfunc that takes in a boolean value. If true return 'Hello' else 'Goodbye'
def myfunc(a):
    if a==True:
        return'Hello'
    else:
        return 'Goodbye'
print(myfunc(True))

# Write a function called myfunc that takes in x,y,z. If z=true return x if z= false return y
def myfunc(x,y,z):
    if z==True:
        return x
    elif z==False:
        return y
print(myfunc('first', 'second', False))

# Write a function called sum that takes in 2 argument adn return their sum
def sum(a,b):
    return a+b
print(sum(4,5))

# Write a function called is_even that takes in 1 argument and return true if even else return false
def is_even(num):
    return num%2==0
print(is_even(5))

# Write a function called is_even that takes in 1 argument and return true if even else return false
def is_greater(num1, num2):
    return num1>num2
print(is_greater(5,5))

# Write a function called sum that takes in an arbitrary number of argumenta and return their sum
def sum(*args):
    sum = 0
    for i in args:
        sum+=i
    return sum
print(sum(4,5,6,7,7,89))

# Write a function called sum that takes in an arbitrary number of argumenta and return a list containing only even arguments
def even_list(*args):
    l = []
    for i in args:
        if i%2==0:
            l.append(i)
    return l
print(even_list(2,3,4,5,6,7))

# Write a function called sum that takes in an arbitrary number of argumenta and return a string with upeercase at even position ald lowercase at odd position
def camel_string(s):
    new_s = ""
    for i in range(len(s)):
        if i%2==0:
            new_s+=s[i].lower()
        else:
            new_s += s[i].upper()

    return new_s
print(camel_string("YaNsh bhardwaj"))

#Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 9 (every 6 will be followed by at least one 9). Return 0 for no numbers.
def summer_69(ar):
    sum = 0
    add = True
    for i in ar:
        while add:
            if i!=6:
                sum+=i
                break
            else:
                add = False
        while not add:
            if i!=9:
                break
            else:
                add=True
                break
    return sum
print(summer_69([4, 5, 6, 7, 8, 9]))
print(summer_69([2, 1, 6, 9, 11]))

# try except
def ask_for_int():
    while True:
        try:
            num = int(input("Enter a number: "))
        except:
            print("This is not a number")
            continue
        else:
            print("Well done! Thank u")
            break
        finally:
            print("Like i will always run")

ask_for_int()