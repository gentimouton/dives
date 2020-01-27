# dives
quick and dirty dives into various datasets

# anaconda setup
- download and install anaconda (it comes with its own python)
- test on Windows: press windows key, type `jupyter` and enter
- if this does not open in browser, [fix it](https://stackoverflow.com/a/46830008)
- if desired (saves 1-2 clicks), [configure notebook directory](https://stackoverflow.com/a/47042617)

# pycharm setup
- download and install regular edition
- [optional] purchase: buy 1 year, receive the licence certificate email, click on activate software. This leads to their site, where you download the activation key (2300 characters ending with `==`). In Pycharm, Help > Register > activation code (should color green).
- to configure interpreter for a new project: pick pure python. Then 1) new env using venv, or 2) existing interpreter (should show none) > click `...` > system interpreter > `C:\Users\YOURNAME\Anaconda3\python.exe`.

# best practices i'm not doing

- use `virtualenv`
- default `%autoreload 2` in notebooks https://stackoverflow.com/a/5399339 (seems to not always work on Windows)
- save dependencies `pip freeze > requirements.txt`
- make modules in python, unit test them, and import them in notebooks
- high-level pickling: Joblib caches return values based on function name and parameters passed.
```python
from sklearn.externals.joblib import Memory
memory = Memory(cachedir='/tmp', verbose=0)

@memory.cache
def computation(p1, p2):
    ...
```

# tricks

- [outlier removal 1-liner](https://stackoverflow.com/a/23202269)
- SettingWithCopyWarning warning from pandas: [explanation and solutions](https://stackoverflow.com/a/20627316) 

