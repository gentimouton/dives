45mins


# analytics

Number of job applications from members is one of many critical metrics that is tracked and important to LinkedIn's job ecosystem. You are going through the weekly jobs dashboard, and the job applications has dipped by 10% site wide in a particular week. How will you proceed to investigate this issue ?



# experimentation

Problem Statement
At LinkedIn, our marketing teams use a variety of email campaigns to our members, to notify them about new product features and to provoke awareness or engagement of one sort or another. We constantly look into ways to optimize the emails to improve the efficiency. Say, we now have some changes for one of the existing emails: it now has a new subject line, and a new email design. 
    
Questions
How would you determine whether the new email is better than the old email?


metrics: open rate, ctr, onsite conv - count 

4 groups 
- pro: can attribute how much of lift comes from subject vs design
- con: less power - more users

power analysis: can only run 2 groups for power  
    

first exp: increase open rate -> change subject line only - we saw little change (small, not sig) in conv 
control = (old,old), treatment1 = (new,old)
how to enroll: |||||||||||||| |||||||||||||
    
second: change subject line and email design -> increase conv
control = (new,old), treatment2 = (new,new)
how to enroll: ||||||- |||||||| - ||||||- |||||||

H: changing email design (controling for subject) increases conv
    
    
    
    
# SQL

Table 1: world_population
 
```
continent    country    population
North America    United States of America    324118787
North America    Canada    36286378
North America    Mexico    128632004
Asia    China    1382323332
Asia    India    1326801576
Asia    Vietnam    94444200
```

Question: find the largest country (in terms of population) in each continent using the table
    
Please use SQL

```sql
select distinct
    continent,
    last_value(country) over(partition by continent order by population asc) as top_country
from world_population w
```

# python

Question - output the country with highest ratio of continent's population:
continent country population pct_of_population
Oceania Australia 24309330  60.9235701

Use python with no library
```python
continent_country_pop = {
    'NA': {
        'USA': 324123456,
        'CA':
    }
}

# first: compute pop for each continent
# continent_pop = {'NA': 324118787+36286378+128632004, 'Asia': 324567894,}
from collections import defaultdict

continent_pop = defaultdict(int)
for continent, countries in continent_country_pop.items():
    continent_pop += sum(countries.values())
    
# step 2: divide each continent_country_pop.value.value by continent_pop.value
continent_pop_ratios = defaultdict(dict)
for continent, countries in continent_country_pop.items():
    for country, pop in countries.items():
        continent_pop_ratios[continent][country] = pop / continent_pop[continent]

        
# step 3: find highest value.value. Output looks like this:
# continent country population pct of population
# Oceania Australia 24309330  60.9235701
top_row = ['','',0,0]

for continent, countries in continent_pop_ratios.items():
    for country, pop_ratio in countries.items():
        if pop_ratio > top_row[3]:
            pop = continent_country_pop[continent][country]
            top_row = [continent, country, pop, pop_ratio]

print("continent\tcountry\tpopulation\tpct of population")
print('\t'.join(top_row))
```
