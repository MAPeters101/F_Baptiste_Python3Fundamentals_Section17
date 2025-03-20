print(1 < 2)
print('A' < 'Z')

def key_func(x):
    return abs(x)

data = [-10, -6, 0, 3, 6]

print(sorted(data))

print([key_func(x) for x in data])

print(sorted(data, key=key_func))
print('-'*80)

data = [2, -2, 1, -1]
print(sorted(data, key=key_func))
print(sorted(data, key=key_func, reverse=True))



print('-'*80)





