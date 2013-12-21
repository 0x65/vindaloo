def curry(x, c=None):
    if c is None:
        c = x.func_code.co_argcount
    x.__curried = True
 
    def p(*a):
        if len(a) > c:
            f = x(*a[:c])
            if getattr(f, '__curried', False):
                f = curry(f)
            return f(*a[c:])
        elif len(a) == c:
            return x(*a)

        def q(*b):
            return x(*(a + b))

        q.__name__ = p.__name__[:-3] + ' -> '.join([''] + [str(b) for b in a])
        return curry(q, c - len(a))
    
    p.__name__ = '%s...' % x.__name__
    return p
