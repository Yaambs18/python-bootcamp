from collections import Counter

list = [1,1,1,1,2,3,3,4,5,5,5,6,6]

c = Counter(list)
print(c)
print(sum(c.values()))

print(Counter('adnbhebfhejfnjsdsnbfjdsbgjhs'))

print(Counter("hi yansh hello yansh how are you".split()))

print(c.most_common(2))