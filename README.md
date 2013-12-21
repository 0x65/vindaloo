Vindaloo
=========

In a language with currying, like Haskell, functions taking multiple arguments (i.e. a function (A x B) -> C) are transformed into functions that take a single argument (i.e. a function A -> (B -> C)). 

This is a Python decorator that does that, just in case you like the overhead of partially applied functions in your code.

```
>>> from vindaloo import curry
>>> id = curry(lambda x: x)
>>> const = curry(lambda x, y: x)
```

We can apply as many or as few parameters as we want.

```
>>> const(3)
<function <lambda> -> 3... at 0x106e97a28>
>>> _(4) == const(3,4)
True
>>> comp = curry(lambda f, g: lambda x: f(g(x)))
>>> id(comp, lambda x: x + 2, lambda x: x * 4, 100)
402
```
