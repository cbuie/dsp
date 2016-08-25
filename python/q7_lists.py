# Based on materials copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0


def match_ends(l):
    def f(x): return len(x) > 1 and  x[:1] ==  x[-1:]
    x = list(filter(f, l))
    return(len(x))

print (match_ends(['aba', 'xyz', 'aa', 'x', 'bbb']))
print (match_ends(['', 'x', 'xy', 'xyx', 'xx']))
print (match_ends(['aaa', 'be', 'abc', 'hello']))

###########################################################################

def front_x (l):
    l.sort()
    xl = [i for i in l if i.startswith('x')]
    for i in xl: l.remove(i)
    return xl + l

print(front_x(['bbb', 'ccc', 'axx', 'xzz', 'xaa']))
print(front_x(['ccc', 'bbb', 'aaa', 'xcc', 'xaa']))
print(front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark']))

###########################################################################


def sort_last(l):
    return sorted(l, key=lambda tup: tup[1])

print(sort_last([(1, 3), (3, 2), (2, 1)]))
print(sort_last([(2, 3), (1, 2), (3, 1)]))
print(sort_last([(1, 7), (1, 3), (3, 4, 5), (2, 2)]))

###########################################################################

def remove_adjacent(l):
    l2 = []
    for i in range(len(l)):
        if (i != len(l) - 1):
            if ((l[i] == l[i + 1])):
                continue
            else:
                l2.append(l[i])

        else:
            l2.append(l[i])
    return l2

print(remove_adjacent([1, 2, 2, 3]))
print(remove_adjacent([2, 2, 3, 3, 3]))
print(remove_adjacent([3, 2, 3, 3, 3]))


###########################################################################

def linear_merge(list1, list2):
    return sorted(list1 + list2)

print(linear_merge(['aa', 'xx', 'zz'], ['bb', 'cc']))
print(linear_merge(['aa', 'xx'], ['bb', 'cc', 'zz']))
print(linear_merge(['aa', 'aa'], ['aa', 'bb', 'bb']))


