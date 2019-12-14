
## source

https://www.interviewqs.com/
- They send questions to a free mailing list Mon/Wed/Fri.
- They send answers the next day to the paid mailing list.
- Topics are: SQL, pandas, python (algo), stats, and ML (rarely).


Example:
```
Sample question 1: Statistical knowledge

Suppose there are 15 different color crayons in a box. Each time one obtains a crayon, it is equally likely to be any of the 15 types (ie draw with replacement). Compute the expected # of different colors that are obtained in a set of 5 crayons. (Hint: use indicator variables and linearity of expectation)

Solution: https://math.stackexchange.com/a/41521

Chance of drawing crayon i at least once in the set of 5: 
Ci = 1-(14/15)^5

Number of unique crayons 
= E[sum(indicator(crayon i))] 
= E[sum(Ci)] 
= 15 * (1- (14/15)^5) = 4.4
```




## useful pandas links

unfuncs: .diff, .shift, .cumsum, .cumcount, 
.str commands (works on strings), .dt commands (works on dates)
https://towardsdatascience.com/pandas-tips-and-tricks-33bcc8a40bb9

cookbook
https://pandas.pydata.org/pandas-docs/stable/user_guide/cookbook.html
