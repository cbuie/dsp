[Think Stats Chapter 5 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2006.html#toc50) (blue men)

>> 34.27 percent of men in the population that fit the blue man criteria. 

```
import scipy.stats
mu = 178;  sigma = 7.7

norm_dist = scipy.stats.norm(loc=mu, scale=sigma)

#height range: 5'10" to 6'1", convert feet to centimeters:

min_height =  (5*12 + 10) *2.54
max_height = (6*12 + 1) *2.54

in_range = dist.cdf(max_height)-dist.cdf(min_height)

print ('%s is the percentage of men in the population that fit the blue man criteria. ' % in_range)

```
