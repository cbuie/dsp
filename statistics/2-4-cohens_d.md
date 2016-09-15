[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)

1rst total weight mean:  7.20109443044
Others total weight mean:  7.32585561497
1rst std:  1.42057287772
other std:  1.39419547621
cohens d -0.0886729270726

The effect size measured by Cohen's d for total weight when comparing 1rst born to others is minimal.  In fact, the diffence is just over 1 oz difference between the two groups.  That means the difference is around 0.7%. In comparison to birth length, birth weight also seems to suggest a weak correlation between any meaningful difference in birth order.

```
#code used, adapted from ThinkStats2 page 24.

print '1rst total weight mean: ' , first.totalwgt_lb.mean()
print 'Others total weight mean: ', others.totalwgt_lb.mean()
print '1rst std: ', first.totalwgt_lb.std()
print 'other std: ', others.totalwgt_lb.std()

Cohen's d  is meant to convey the size of the effect by comparing the mean diff. between two groups to the
variablility within the two groups (pooled std dev).  

def cohens_d(grp1, grp2):
    import math
    mean_diff = grp1.mean() - grp2.mean()
    
    var1 = grp1.var(); var2 = grp2.var()
    n1 = len(grp1); n2 = len(grp2)
    
    pooled_var = (n1 * var1 + n2 * var2)/ (n1 + n2)
    d = mean_diff / math.sqrt(pooled_var)
    return d

print'cohens d', cohens_d(first.totalwgt_lb,others.totalwgt_lb)
```
