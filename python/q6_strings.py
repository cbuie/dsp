# Based on materials copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0


def donuts(count):
    '''
    input must be an int
    :param count:
    '''

    try:
        if int(count) < 10:
            print "Number of dounts: %s" %count
        else:
            print "Number of donuts: many"
    except:
        raise NotImplementedError('input must be a number')

# test it out:
for i in range(1,20,2):donuts(i)
    
########################################################################
def both_ends(s):
    '''
    :param s: input a string
    :return: first 2 chars and last 2 chars
    '''
    try:
        if len(s) > 2:
            return s[:2]+s[-2:]
        elif len(s) <= 2:
            return ''
    except:
        raise NotImplementedError('input was not an int')

# test it out:
for i in str('here are a bunch of words to test').split(): print both_ends(i)

########################################################################


def fix_start(s):
    s0 = s[0]
    return s0+s[1:].replace(s[0],'*')
    
print fix_start('babble')
print fix_start('aardvark')
print fix_start('google')
print fix_start('donut')

########################################################################

def mix_up(a,b):
    if len(a) + len(b)>4:
        a0 = (a[:2]);b0 = (b[:2])
        return a.replace(a0,b0)+' '+b.replace( b0,a0)
    else:
        raise ValueError('both arguments be at least 2 chars long')

print mix_up('mix', 'pod')
print mix_up('dog', 'dinner')
print mix_up('gnash', 'sport')
print mix_up('pezzy', 'firm')
print mix_up('a','b')

########################################################################

def verbing(s):
    if len(s)>2:
        if s[3:] == 'ing':
            return s.__add__('ly')
        else:
            return s.__add__('ing')
    else:
        return s

print verbing('hail')
print verbing('swiming')
print verbing('do')

########################################################################

def not_bad(s):
    try:
        n = s.rindex('not'); b = s.rindex('bad')+3
        if n<b:
            return s.replace(s[n:b],'good')
        else:
            return s
    except:
            return s


print not_bad('This movie is not so bad')
print not_bad('This dinner is not that bad!')
print not_bad('This tea is not hot')
print not_bad("It's bad yet not")


def front_back(a, b):
    """
    Consider dividing a string into two halves. If the length is even,
    the front and back halves are the same length. If the length is
    odd, we'll say that the extra char goes in the front half. e.g.
    'abcde', the front half is 'abc', the back half 'de'. Given 2
    strings, a and b, return a string of the form a-front + b-front +
    a-back + b-back

    >>> front_back('abcd', 'xy')
    'abxcdy'
    >>> front_back('abcde', 'xyz')
    'abcxydez'
    >>> front_back('Kitten', 'Donut')
    'KitDontenut'
    """
    raise NotImplementedError
