#!/usr/bin/env python3
"""Simple decoder using Fibonacci spacing for Hebrew text."""
from typing import Iterable

# Fibonacci sequence generator
def fibonacci_sequence(n: int) -> Iterable[int]:
    a, b = 1, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# Load Hebrew text from file
with open('glyphs/example_hebrew.txt', 'r', encoding='utf-8') as f:
    text = f.read().replace('\n', '')

# Determine how many letters to extract
# We'll generate Fibonacci numbers up to the length of the text
fib_numbers = list(fibonacci_sequence(len(text)))

result = []
for pos in fib_numbers:
    if pos - 1 < len(text):
        result.append(text[pos - 1])
    else:
        break

print(''.join(result))
