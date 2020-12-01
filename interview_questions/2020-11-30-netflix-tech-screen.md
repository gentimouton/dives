# Stats

We want to run an A/B test. We take a random sample of 100k Netflix members and assign them to cell A. 
We take another random sample of 100k Netflix members and assign them to cell B. 
We let the experiment run for 3 months and measure retention. 
A member is considered retained if she hasn't cancelled her subscription at the end of these 3 months.

## Question 1

Here are the results we observe. What would you conclude for this experiment?
- CELL A: Sample size 100k, retention = 80%
- Cell B: Sample size 100k, retention = 80.2%

Answer: 
- chi2 test (works for ratios of individuals)
- or bootstrap/permutation test (works for any kind of metric)
- null hypothesis: there's no difference in proportions between groups A and B
- method: tabulate retained vs churned, and group A vs B
- observed (B) vs expected (A)
- compute chi2 using formula I don't remember, something like (obs-exp)/exp 
- lookup pvalue from value of chi2 distribution for df=100k
- if pvalue < threshold (.05), reject null

## Question 2
Assume you’ve run a test and the resulting p-value is 25%. 
How would you describe (in words) what this value means? 
What would you recommend that a stakeholder should conclude based on these results?

Answer:
- Comparing more cells would increase N, which decreases variance
- p-value = P(observed effect > "random grouping" effect)

## Question 3
Assume we observe the same results on retention but sample size is 200k. 
Would the p-value be smaller or larger or the same? Why?

Answer:
- Increasing sample size means smaller variance, and smaller p (sqrt proportion)

## Question 4
Assume we have sample size of 100k, and still a delta in 0.2% but the baseline retention rate is 50%. 
Would the p-value be smaller or larger or the same? Why?
- CELL A: Sample size 100k, retention = 50%
- Cell B: Sample size 100k, retention = 50.2%

Answer:
- I was at first thinking .2/80 < .2/50, thus p would be smaller. 
But thinking about retention as churn means .2/20 is another way to look at the lift, and .2/20 > .2/50
- Math wise, variance is proportional to p(1-p), so the closer p is to 50%, the higher the variance.


## Question 5
We are interested in measuring the difference in median streaming hours. Given the following table, what can you say about the impact of the test experience on median streaming? Would your answer be different if you knew the streaming hours for each account in the test?
- CELL A: Sample size 100k, median streaming = 40
- Cell B: Sample size 100k, median streaming = 42

Answer:
- Knowing each account's MW would allow us to compute "variance"
- It would allow us to bootstrap accounts and build a confidence interval
- Brown-mood (sp?) test for median/percentiles

5b: Explain bootstrap
```
n_iterations = 1000 # good for p-values of .05
medians = []

for iteration in range(n_iterations):
  A' = sample with replacement from A
  B' = sample with replacement from B
  compute medians for A' and B'
  medians.append(A' - B')
  
histogram(medians)
p = min(argmin(0), 1-argmin(0))/2
```




# SQL

We have the following 2 tables.
Customers table (one row per customer)
```
customer_id 
signup_date
``` 

Viewing table (one row per video,customer,watch_date)
```customer_id
video_id
watch_date
watch_duration_minutes
```

Write a SQL query to get a list of customer id who watched total less than 3 hours within the first 7 days after signup.
```sql
with customer_watch_behavior_daily as (
select
  customer_id,
  watch_date,
  sum(watch_duration_minutes) as mw
from viewing
group by 1,2
)

select 
  c.customer_id,
  sum(w.mw) as mw
from customers c
left join customer_watch_behavior_daily w
  on c.customer_id = w.customer_id
  and datediff('day', c.signup_date, w.watch_date) <= 7
group by 1
having sum(mw) <= 3*60
```


# Metrics

Suppose that we are testing adding a new row, “Watch with the Whole Family”, containing titles that are appropriate for family viewing.
Like the other rows, this row’s position will vary from user to user, with the position determined by a personalized algorithm. 
We observe a streaming decrease in the cell with the added row, but the significance is moderate (p=.04). 
What other data could we look at to strengthen or weaken the evidence that adding the extra row caused a streaming decrease?
- Cell A: Control experience (standard rows)
- Cell B: Test experience (standard rows + “Watch with the Whole Family”)

Answer: explanatory metrics 
- number of impressions for this row per user enrolled in cell B
- % of B users with an impression of the row -- if this is 50%, our eligible-user "effect size" is double what we measure for all users
- bootstrap envelope - x axis = percentile of HW, y axis is effect, plot confidence interval up/low
- HTE - new users, countries, platform

non-metric alternative: 
- filter enrollment to users who see the carousel -- problem: no counterfactual in control. Solution: fire counterfactual event
