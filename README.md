# Anagrm

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
[![ForTheBadge built-with-love](http://ForTheBadge.com/images/badges/built-with-love.svg)](https://GitHub.com/Rippr/)
[![ForTheBadge uses-badges](http://ForTheBadge.com/images/badges/uses-badges.svg)](http://ForTheBadge.com)

Optimized anagram solver written in Python.

## How to use Anagrm

1. Populate dictionary.txt with all valid words. Each line should contain a single word.
2. Run generate_patterns.py. This will probably take a while.
3. Add all the words to be unscrambled in input.txt. Again, each line should contain a single word.
4. Finally, run anagrm.py.


## How does Anagrm work?

A naive anagram solver would simply generate all permutations of the input string, and check if a permutation is valid.
Using a conventional list to store the dictionary words would make it extremely inefficient.  

A simple optimization is to store the words as a Hash Table.
This allows for O(1) lookups and greatly reduces the runtime.  

However, hashes for every single permutation would still have to be generated.
Instead of hashing the input string directly, Anagrm lexicographically sorts the letters in the input string.
Thus, all possible permutations of the string will resolve to a single value, which can be checked efficiently.  

generate_patterns.py takes each word in the dictionary, lexicographically sorts its letters,
and maps the resultant string to the initial one.
This precomputed data is stored as a Python dictionary\[str, list\[str\]\] in patterns.py.
The same computation is done for each input string in input.txt and all valid results are printed.


### Complexity

n: Number of input words  
m: Number of dictionary words  
k: Average word length  

- Naive solution
  - Runtime Complexity: O(n * m * k!)
- Hash Table solution
  - Runtime Complexity: O(n * k!)
- Anagrm
  - Precomputation Complexity: O(m * k!)  
  - Runtime Complexity: O(n * klogk)
