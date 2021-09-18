print(bin(1024))

print(hex(1024))

print(round(5.23222,2))

s = "hello how are you mary? are you felling okay?"
print(s.islower())

s2 = 'tswguwtwswtdydtwtdwldhdywwwwswxsw'
print(s2.count('w'))


set1 = {2,3,1,5,6,8}
set2 = {3,1,7,5,6,8}

print(set1.difference(set2))
print(set1.union(set2))

dictionary = {x:x**3 for x in range(5)}
print(dictionary)

list1 = [1,2,3,4]
list1.reverse()
print(list1)

list2 = [3,4,2,5,1]
list2.sort()
print(list2)