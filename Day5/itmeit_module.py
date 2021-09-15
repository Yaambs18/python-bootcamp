import timeit

stmt1 = '''
func_one(100)
'''

setup1 = '''
def func_one(n):
    return [str(i) for i in range(n)]
'''

print(timeit.timeit(stmt1, setup1, number=100000))

stmt2 = '''
func_two(100)
'''

setup2 = '''
def func_two(n):
    return list(map(str, range(n)))
'''

print(timeit.timeit(stmt2, setup2, number=100000))