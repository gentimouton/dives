
Prototypes of statistical concepts

# experiment analysis
- stratified exp analysis
- 2 stage least square
- heterogeneous treatment effects
- response surface 
- CUPED, covariates, stratify to reduce within-group variance. Achieve significance faster. Efficient covariates are those that vary a lot across the user base. Experiment’s output metric during pre-period is an efficient covariate too.
See [Microsoft 2013](https://www.exp-platform.com/Documents/2013-02-CUPED-ImprovingSensitivityOfControlledExperiments.pdf), 
[degen state](http://www.degeneratestate.org/posts/2018/Jan/04/reducing-the-variance-of-ab-test-using-prior-information/), 
[stats geek](http://thestatsgeek.com/2014/02/01/adjusting-for-baseline-covariates-in-randomized-controlled-trials/),
[clevenger](https://www.slideshare.net/JohnClevenger4/clevenger-experimentation-meetup),
[dean eckles](http://www.deaneckles.com/blog/745_using-covariates-to-increase-the-precision-of-randomized-experiments/).
- [Detecting Network Effects: Randomizing Over Randomized Experiments](http://web.media.mit.edu/~msaveski/assets/publications/2017_detecting_network_effects/paper.pdf)
- concrete examples of [Common Pitfalls in Online Controlled Experiments](http://exp-platform.com/Documents/2017-08%20KDDMetricInterpretationPitfalls.pdf)
- [Percentile bootstrapped enveloppes](https://medium.com/netflix-techblog/streaming-video-experimentation-at-netflix-visualizing-practical-and-statistical-significance-7117420f4e9a).
Instead of comparing mean/median/p90 between 2 groups, compute a conf interval 
for each of the 100 percentiles, and Bonferroni-adjust them. 

# sequential testing/multiple comparisons
- [Dunnet's test](https://en.wikipedia.org/wiki/Dunnett%27s_test)
- [Newman-Keuls](https://en.wikipedia.org/wiki/Newman%E2%80%93Keuls_method). 
Assume homoscedasticity. Alternative to Bonferroni correction.
Run Anova first, if you find a sig diff, sort the G groups by their means, quasi-t-test* rank 1 vs rank G. 
If sig, keep running NK on the G-1 groups. 
If not sig, no need to continue: the only sig differences to report are those strictly above rank G. 
- [Tukey-Kramer](https://www.statisticshowto.datasciencecentral.com/tukey-test-honest-significant-difference/).
Assume homoscedasticity. Alternative to Bonferroni correction.
Similar as NK, but works with different sample sizes. 
For each possible pair of groups, compute HSD (similar to t-test).  
[Link](https://dnett.public.iastate.edu/S611/35TukeyNA.pdf)
- Peaking, mixture sequential probability ratio test, Fixed horizon vs sequential testing.
[Optimizely KDD 2017](http://www.kdd.org/kdd2017/papers/view/peeking-at-ab-tests-why-it-matters-and-what-to-do-about-it)
- Delete-a-group jackknife DAGJK: unbiased variance estimator, and faster than jackknife. 
[Useful when sequential testing](https://eng.uber.com/xp/).
Also relevant when combining stratified samples.
[Original 2001 paper](http://www.sverigeisiffror.scb.se/contentassets/ca21efb41fee47d293bbee5bf7be7fb3/the-delete-a-group-jackknife.pdf),
[R package](https://www.istat.it/en/methods-and-tools/methods-and-it-tools/process/processing-tools/ever).

# tests
- [spearman: assumptions, what it tests, when it differs from pearson](https://statistics.laerd.com/statistical-guides/spearmans-rank-order-correlation-statistical-guide.php)
- [Ratio t-test](https://www.graphpad.com/guides/prism/7/statistics/stat_paired_or_ratio_t_test.htm?toc=0) vs t-test on difference.
- [Welch’s T-test](https://en.wikipedia.org/wiki/Welch%27s_t-test#Examples)
and Homoscedasticity. Plot wrongness of t-test against difference in variances.
- [Brown-Mood median test](https://en.wikipedia.org/wiki/Median_test)
[Lacks power](https://www.tandfonline.com/doi/abs/10.1080/00031305.2000.10474539) for small sample sizes.
- [Mann–Whitney U test](https://en.wikipedia.org/wiki/Mann%E2%80%93Whitney_U_test#Examples). 
Compare robustness to outliers vs t-test. How to report effect size and significance?
- [test selection](https://www.graphpad.com/support/faqid/1790/) to describe, compare, quantify association or predict a measurement (eg gaussian), rank, binomial, or survival time variable.

# inference
- propensity score matching
- regression adjustment (vs prop score matching)
- regression discontinuity
- diff in diff
- [Causal inference using regression on the treatment variable](http://www.stat.columbia.edu/~gelman/arm/chap9.pdf)
- bayesian alternative to hyp testing, pymc3
- causal impact lib

# modeling
- [addressing colinearity](https://stats.stackexchange.com/a/56531), and example when/why it is a problem
- regressing right: 
[good code](https://github.com/justmarkham/DAT4/blob/master/notebooks/08_linear_regression.ipynb)
[cheat sheet](https://songhuiming.github.io/pages/2016/07/12/statsmodels-regression-examples/)
- generalized linear models
- generalized additive models
- [other linear models](https://bashtage.github.io/linearmodels/)
- hierarchical modeling 
- [introduction to modeling](https://bbolker.github.io/math3mb/)
- [overview of model explainability](https://towardsdatascience.com/an-overview-of-model-explainability-in-modern-machine-learning-fc0f22c8c29a)

# algorithms
- [Fast bootstrap](https://medium.com/netflix-techblog/streaming-video-experimentation-at-netflix-visualizing-practical-and-statistical-significance-7117420f4e9a) from Netflix by histogramming the sample and Poisson drawing from it.
- [T-digest](https://github.com/CamDavidsonPilon/tdigest) compute percentiles for streaming data. Additive, thus parallelizable.
- [non-negative matrix factorization](https://datascience.stackexchange.com/questions/10299/what-is-a-good-explanation-of-non-negative-matrix-factorization )
produces topics from term-document matrix. 
- [locality-sensitive hashing](https://blog.mayflower.de/6498-lsh-nearest-neighbour-search.html)
Solve approximate or exact Near Neighbor Search in high dimensional spaces. 
http://www.mit.edu/~andoni/LSH/ 

# time series
- ARIMA
- prophet
- SAX representation and aggregation
- [survival analysis](https://data.princeton.edu/pop509/), [Gillen's class](https://eee.uci.edu/11s/37910), 
and [intro book](http://www.biecek.pl/statystykaMedyczna/Stevenson_survival_analysis_195.721.pdf)
- [proportional hazard model - cox model](https://en.wikipedia.org/wiki/Proportional_hazards_model#The_Cox_model)
- [forecasting ebook](https://otexts.com/fpp2/stl.html)

# clustering
- hierarchical clustering with fixed-size buckets
- kmeans silhouette, inertia analysis, and other methods to justify `k`
- affinity clustering

# viz
- Ternary plot. Each data point has 3 percentages, summing up to 100%. Plot points within a triangle.
- [viz examples](https://serialmentor.com/dataviz/index.html)

# misc
- market basket analysis, compare algorithms for [association rule mining](https://en.wikipedia.org/wiki/Association_rule_learning#Other_types_of_association_rule_mining), 
[intro + data](https://towardsdatascience.com/a-gentle-introduction-on-market-basket-analysis-association-rules-fa4b986a40ce)
- end-to-end spam detector: stemmer, naive bayes, flask frontend
- recommender using nearest neighbor
- recommender using collaborative filtering
- recommender using neural net embeddings
- OCR via CNN in pytorch
- reinforcement learning
- GAN
- computer vision: label dog vs cat
- optimized risk scores [paper](https://blog.acolyer.org/2019/11/01/optimized-risk-scores/)
- [herfindhal index](https://github.com/econpy/search_engine_hhi)
- [rand index](https://en.wikipedia.org/wiki/Rand_index)
- [Mahalanobis_distance](https://en.wikipedia.org/wiki/Mahalanobis_distance): when to use, and difference vs euclidean vs manhattan
- [basic DS concepts](https://www.amazon.com/Practical-Statistics-Data-Scientists-Essential/dp/1491952962#reader_1491952962)

