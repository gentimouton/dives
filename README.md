# dives
quick and dirty dives into various datasets


# best practices i'm not doing

- use `virtualenv`
- save dependencies `pip freeze > requirements.txt`
- high-level pickling: Joblib caches return values based on function name and parameters passed.
```python
from sklearn.externals.joblib import Memory
memory = Memory(cachedir='/tmp', verbose=0)

@memory.cache
def computation(p1, p2):
    ...
```
