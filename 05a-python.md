# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

###Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>>
The most important distinction between a list and a tuple is that a tuple is not mutable and a list is mutable.
Because dictionary keys must be immutable, in certain situation you can use tuples as dictionary keys. However, list can never be used as keys in
dictionaries. The list data structure has several methods tuples do not. Most notably list have the append, extend, remove, and pop.

---

###Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>>
A list keeps order data and a set does not, when you care about order you have to use a list. Sets and lists are similar in that they both only contain values. This is different than dictionaries that uses the key value system. Sets require items to be hashable, list do not. If you have non-hashable items you cannot use a set and must use a list. Sets forbid duplicates, list do not. Checking for membership of a value in a set (or dict, for keys) is much faster (remaining relatively constant despite size of the set), while in a list it takes time proportional to the list's length. The difference is a set is hashable while a list is not.

###Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>>
To generalize, a lambda function is a function that takes any number of arguments and returns the value of a single expression. Lambda functions cannot contain commands, and they cannot contain more than one expression.
Lambda functions are a matter of style. Using them is never required; anywhere you could use them, you could define a separate normal function and use that instead. You can use them in places where you want to encapsulate specific,
non-reusable code without littering your code with a lot of little one-line functions.
ex: multiples_of_three = filter(lambda x: x % 3 == 0, [1, 2, 3, 4, 5, 6, 7, 8, 9])

---

###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>>
Source: https://docs.python.org/2/tutorial/datastructures.html
List comprehensions provide a concise way to create lists. Common applications are to make new lists where each element is the result of some operations applied to each member of another sequence or iterable,
or to create a subsequence of those elements that satisfy a certain condition. A list comprehension consists of brackets containing an expression followed by a for clause, then zero or more for or if clauses.
The result will be a new list resulting from evaluating the expression in the context of the for and if clauses which follow it. There are three built-in functions that are very useful when used with
lists: filter(), map(), and reduce(). filter(function, sequence) returns a sequence consisting of those items from the sequence for which function(item) is true. If sequence is a str, unicode or tuple,
the result will be of the same type; otherwise, it is always a list.

filter(), as its name suggests, filters the original iterable and retents the items that returns True for the function provided to filter().map() on the other hand, apply the supplied function to each element of the iterable and return a list of results for each element.

```
#map vs filter

def f(x): return x % 2 != 0 and x % 3 != 0
map(f, range(11)) #the ones that returns TRUE are 1, 5 and 7

#[False, True, False, False, False, True, False, True, False, False, False]

filter(f, range(11)) #So, filter returns 1, 5 and 7

#[1, 5, 7]

squares = [x**2 for x in range(10)]  #list comp
squares_dict = {x: x**2 for x in (2, 4, 6)} #dictionary comp
squares = map(lambda x: x**2, range(10)) #map
```

---

###Complete the following problems by editing the files below:

###Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
from datetime import datetime

date_start = "01-02-2013"
date_stop = "07-28-2015"

d1 = datetime.strptime(date_stop, "%m/%d/%Y")
d2 = datetime.strptime(date_start, "%m/%d/%Y")
print d2 - d1


```

>> 937 days, 0:00:00

b.  
```
date_start = '12312013'  
date_stop = '05282015'  

from datetime import datetime


d1 = datetime.strptime(date_stop, "%m%d%Y")
d2 = datetime.strptime(date_start, "%m%d%Y")
print d1-d2
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE (answer will be in number of days)

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> 513 days, 0:00:00

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

###Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

###Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

###Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)





