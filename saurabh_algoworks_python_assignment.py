#!/usr/bin/env python
# coding: utf-8

# In[23]:


# using user define function, count the no. of element in list

def Freq(my_list): 
    count = {}
    for item in my_list:
        if (item in count):
            count[item] += 1
        else:
                count[item] = 1
    for key, value in count.items():
        print("% d -> % d" % (key, value))


if __name__ =="__main__":
    my_list =[1,4,2,6,2,4,1,2] 
    Freq(my_list) 


# In[14]:


# using in_built function, count the no. of element in list


import collections
x=[1,4,2,6,2,4,1,2]
y=collections.Counter(x)
print(y)


# In[22]:


#To find duplicate element in list



def dupl(list_a):
    exist = set()
    for n in list_a:
        if n in exist:
            print ("duplicate:", n)
        else:
            exist.add(n)
            
list_a=[1, 2, 4, 2, 5, 6, 7]
dupl(list_a)


# In[43]:


#fibonacci by recursion using caching to avoid duplication.


import functools

@functools.lru_cache(None)
def fib(n):
    
        if n < 2:
            return n
        return fib(n-1) + fib(n-2)
    
n=7
fib(n)
for n in range(0,n):
    print(fib(n))


# In[57]:


#Decorator to call a number of time functions called.

import functools
from scipy import integrate

def counted_calls(f):
    @functools.wraps(f)
    def count_wrapper(*args, **kwargs):
        count_wrapper.count += 1
        return f(*args, **kwargs)
    count_wrapper.count = 0
    return count_wrapper

def f(x): return x**2

wrapped = counted_calls(f)
integrate.quad(wrapped, 0, 1)
print(wrapped.count)


# 
