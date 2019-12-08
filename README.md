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


# TODO

Demos of the following topics
- propensity score matching
- regression discontinuity, diff in diff
- herfindhal index https://github.com/econpy/search_engine_hhi
- rand index https://en.wikipedia.org/wiki/Rand_index
- https://en.wikipedia.org/wiki/Mahalanobis_distance: when to use, and diff vs euclidean vs manhattan
- hierarchical clustering with fixed-size buckets
- methods to find the "right" k in kmeans
- glm https://bbolker.github.io/math3mb/
- [pandas: remove outliers](https://stackoverflow.com/a/23202269)
- doing lin reg right: [addressing colinearity](https://stats.stackexchange.com/a/56531), [good code](https://github.com/justmarkham/DAT4/blob/master/notebooks/08_linear_regression.ipynb), [cheat sheet](https://songhuiming.github.io/pages/2016/07/12/statsmodels-regression-examples/)
- SettingWithCopyWarning warning from pandas: [explanation and solutions](https://stackoverflow.com/a/20627316) 


Experimentation stuff
- 2SLS and reducing variance
- [Detecting Network Effects: Randomizing Over Randomized Experiments](http://web.media.mit.edu/~msaveski/assets/publications/2017_detecting_network_effects/paper.pdf)
- [Reducing the Variance of A/B Tests Using Prior Information](http://www.degeneratestate.org/posts/2018/Jan/04/reducing-the-variance-of-ab-test-using-prior-information/)
- [Causal inference using regression on the treatment variable](http://www.stat.columbia.edu/~gelman/arm/chap9.pdf)
- [Adjusting for baseline covariates in randomized controlled trials](http://thestatsgeek.com/2014/02/01/adjusting-for-baseline-covariates-in-randomized-controlled-trials/)
- best practices: [A Dirty Dozen: Twelve Common Metric Interpretation Pitfalls in Online Controlled Experiments](http://exp-platform.com/Documents/2017-08%20KDDMetricInterpretationPitfalls.pdf)
