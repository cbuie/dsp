[Think Stats Chapter 4 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2005.html#toc41) (a random distribution)

>> REPLACE THIS TEXT WITH YOUR RESPONSE

![Alt text](https://github.com/cbuie/dsp/blob/master/random%20cdf.png?raw=true "Random CDF")

![Alt text](https://github.com/cbuie/dsp/blob/master/random%20pmf.png?raw=true "Random PMF")

```
import random
import thinkstats2
import thinkplot

def create_random(n):
    mylist = []
    for i in range (n):
        mylist.append(random.random())
    return mylist

mylist = create_random(1000)

pmf = thinkstats2.Pmf(mylist)
thinkplot.Pmf(pmf, label='random pmf')
thinkplot.show()

cdf = thinkstats2.Cdf(mylist)
thinkplot.Cdf(cdf, label='random cdf')
thinkplot.show()
```
