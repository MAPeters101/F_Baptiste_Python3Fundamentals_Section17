
data = [1, -2, 3, -4, 5, -6]
print(sorted(data))
print(min(data))
print(max(data))
print()

print(sorted(data, key=abs))
print(min(data, key=abs))
print(max(data, key=abs))
print('-'*80)



