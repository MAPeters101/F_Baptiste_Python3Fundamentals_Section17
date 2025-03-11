'''
Question 2
Given the following data:

suits = 'shdc'  # Spades, Hearts, Diamonds, Clubs
ranks = list('23456789') + ['10', 'J', 'Q', 'K', 'A']
Write a function that given those two inputs, returns a list with all 52 cards,
i.e.

[
  ['2s', '3s', ..., 'Ks', 'As'],
  ['2h', '3h', ..., 'Kh', 'Ah'],
  ...
]
Then, enhance this function so that an optional argument can be used to specify
whether the cards in each suit should be sorted in ascending or descending rank
order (assume A has the highest rank in its suit).
'''