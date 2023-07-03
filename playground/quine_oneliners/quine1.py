#quine - no input and produces a copy of its own source
#%s prints the str() of an object (What you see when you print(object)).
#%r prints the repr() of an object (What you see when you print(repr(object))
s='s=%r;print(s%%s)';print(s%s)
