# Binary Search

While a simple search verify each item within a list with a step of 1 and then on each iteration exclude just 1 number, the binary search verify the middle of the list, excluding, on each step, half of the possibilities.

>IMPORTANT: In order to implement a binary search, the list must be sorted.

For comparison, a table considering the worst cases in both simple and binary search:

| Simple Search | Binary Search |
| ----------- | ----------- |
| 100 items -> 100 steps | 100 items -> 7 steps |
| 10000 items -> 10000 steps | 10000 items -> 14 steps |
| 4 billion items -> 4 billion steps | 4 billion items -> 32 steps |

> In Big O notation, the simple search has a **O(n)** runtime, while the binary search has a runtime of **O(log n)**.
