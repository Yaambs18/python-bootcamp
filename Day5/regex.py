import re

text = "My name is yansh bhardwaj"
pattern = "yansh"

print(re.search(pattern, text))

new_text = "my name is yansh, i am yansh, u can call me yansh"

print(re.search(pattern, new_text))

print(re.findall(pattern, new_text))

for match in re.finditer(pattern, new_text):
    print(match)
    print(match.group())
    print(match.span())

text2 = "My phone number is 367-238-2332"
print(re.search(r'\d{3}-\d{3}-\d{4}',text2))
pattern2 = re.compile(r'(\d{3})-(\d{3})-(\d{4})')

result = re.search(pattern2, text2)
print(result.group())
print(result.group(1))
print(result.span())
print(result.group(2))




num_text = "there are 3 numbers. but i don't have 45 numbers, can i ask for 3 numbers?"

pat = re.findall(r"[^\d]+",num_text)
pat1 = re.findall(r"[\d]+",num_text)
print(pat)
print(pat1)