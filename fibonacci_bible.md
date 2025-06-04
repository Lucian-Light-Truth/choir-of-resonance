# Fibonacci Hebrew Decoder

This repository now includes a simple demonstration for exploring a "spacing" cipher using the Fibonacci sequence. The example uses a single verse from the Hebrew Bible.

## Running the Decoder

1. Review `glyphs/example_hebrew.txt` for the source verse (Genesis 1:1).
2. Execute `python3 glyphs/fibonacci_decode.py` to see the letters selected using Fibonacci spacing.

The script steps through the text using 1, 1, 2, 3, 5, 8... offsets and prints the resulting string. This offers a starting point for further experimentation.
