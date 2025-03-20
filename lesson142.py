data = list(range(1,11))
print(data)

def is_even(n):
    return n%2 == 0

evens = [n for n in data if is_even(n)]
print(evens)
print('-'*80)

evens = (n for n in data if is_even(n))
print(list(evens))
print(list(evens))
