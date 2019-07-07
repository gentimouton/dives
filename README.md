# dives
quick and dirty dives into various datasets


# best practices i'm not doing

- use `virtualenv`
- default `%autoreload 2` in notebooks https://stackoverflow.com/a/5399339 (seems to not always work on Windows)
- save dependencies `pip freeze > requirements.txt`
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
