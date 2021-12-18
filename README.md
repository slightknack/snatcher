# snatcher
Silly programming language where *everything* is just pattern matching:

```python
fib
n: (n < 2)
   True: n
n: (fib (n - 1)) + (fib (n - 2))
```
