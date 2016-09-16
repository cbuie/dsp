[Think Stats Chapter 3 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2004.html#toc31) (actual vs. biased)




![Alt text](https://github.com/cbuie/dsp/blob/master/bias%20vs%20unbias.png?raw=true "Biased vs Unbiased")



Unbiased mean: 1.02420515504 
Biased mean: 2.40367910066

code used to compute the answeres.
```

import chap01soln
import thinkstats2
import thinkplot

resp = chap01soln.ReadFemResp()


pmf = thinkstats2.Pmf(resp.numkdhh)


thinkplot.Pmf(pmf, label='numkdhh')
thinkplot.Show()


def BiasPmf(pmf, label=''):

    new_pmf = pmf.Copy(label=label)

    for x, p in pmf.Items():
        new_pmf.Mult(x, x)

    new_pmf.Normalize()
    return new_pmf


biased = BiasPmf(pmf, label='biased')


thinkplot.PrePlot(2)
thinkplot.Pmfs([pmf, biased])
thinkplot.Show()

print pmf.Mean(), biased.Mean()


```
