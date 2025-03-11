'''
Question 3
Suppose we are given some data consisting of symbols (the keys in the
dictionary) and values being a tuple containing Open/High/Low/Close values for
that symbol.

For example:

data = {
    'S1': (100, 200, 80, 180),
    'S2': (10, 20, 8, 18),
    'S3': (50, 150, 50, 150)
}
Write a function that given this data as input, returns the symbol whose
high - low is smallest.

Expand on your function so that it will either return the symbol with smallest
or largest high/low difference, based on an extra argument passed to the
function.
'''