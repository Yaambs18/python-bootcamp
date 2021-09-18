try:
    print(a)  
except NameError:
    print ("Name errror occured")
    try:
        print(1/0)
    except:
        print("ZeroDivision error occured ")
    
finally:
    try:
        l = [1,2,3,4]
        print(l[4])
    except :
        print("IndexOutOfBound error occured")

    print("But Noone can stop me from execution")