#!/usr/bin/env python
# coding: utf-8

# In[7]:


import numpy as np
import math
import time

#problem 1

def oddsum(n):
    sum = 0
    for i in range(0,n):
        if np.mod(i,3) == 0 or np.mod(i,5) == 0:
            sum += i
    return sum

#oddsum(1000)


# In[32]:


#problem 2

#generated fibonacci sequence up to a number less than n 
def fib(n):
    fib = [0,1]
    i = 0
    while fib[-1] < n:
        fib.append(fib[i] + fib[i+1])
        i += 1
    return fib[0:-1]

#sums the even entries of an array
def evensum(array):
    sum = 0
    for i in range(0,len(array)):
        if array[i] % 2 == 0:
            sum += array[i]
    return sum

#not the fastest way to solve the problem, but it is useful to have all of the fibonacci numbers.

#print(fib(4000000))
#evensum(fib(4000000))


# In[90]:


#problem 3

#following two functions compute all the prime factors of a number. Just for fun 
def isprime(n):
    for i in range(1,n-1):
        if n % i == 0 and i != 1:
            return False
    else: 
        return True

def primefactors(num, input_type = int):
    if num - math.floor(num)  != 0:
        print('please enter an integer')
        return
    factors = []
    num = int(num)
    for i in range(2,int(math.sqrt(num))):
        if isprime(i) == True and num % i == 0:
            factors.append(i)
            primefactors(num/i)
    return [num] if factors == [] else factors


#the real deal 
def lpf2(n):
    i = 2
    #getting rid of composite factors. Recall that a factor of n cannot be greater than sqrt(n).
    for i in range(2, int(math.sqrt(n))):
        if n % i == 0:
            n = n / i
    return n


# In[154]:


#problem 4

#checks if a number is a palindrome
def ispal(n):
    for i in range(0,math.floor(len(str(n))/2)):
        if str(n)[i] != str(n)[-(i+1)]:
            return False
    return True

def pal(num1,num2):
    max = 0
    for i in range(num1, int(num1/2), -1):
        for j in range(num2, int(num1/2), -1):
            if ispal(i*j) == True:
                if i*j > max:
                    max = i*j
    return max
    
#pal(999,999)


# In[162]:


#problem 5

np.lcm.reduce(np.arange(50)[1:])


# In[11]:


#problem 6

#returns the sum of squares
def sumsquare(n):
    sum = 0
    for i in range(1,n+1):
        sum += i
    return sum * sum

#returns the square of sum
def squaresum(n):
    sum = 0
    for i in range(1,n+1):
        sum += i*i
    return sum

#sumsquare(100)-squaresum(100)


# In[95]:


#problem 7

#function using brute force
def primecounter(n):
    start_time = time.time()
    primelist = []
    i = 2
    while len(primelist) < n:
        if isprime(i) == True:
            primelist.append(i)
        i += 1
    print("--- %s seconds ---" % (time.time() - start_time))
    return primelist[-1]
    

#primecounter(10001)

#sieve
def sieve(n):
    integers = [i for i in range(1,n)]
    for p in range(2,n):
        k = 2
        while p*k < n:
            try:
                integers.remove(p*k)
                k += 1
            except ValueError:
                k += 1
    return integers

#now the n'th prime finder, using a modified version of sieve
#can't get it to work faster. Slower than brute force
def primecounter_sieve(n, l = 2, h = 100, primes = np.array([])):
    start_time = time.time()
    integers = np.arange(l,h)
    #print(primes)
    #print(integers)
    for p in range(2,h):
        k = 2
        while p*k < h:
            try:
                integers = integers[integers != p*k]
                k += 1
            except ValueError:
                k += 1
    #print(integers)
    primes = np.append(primes, integers)
    #print(primes)
    if len(primes) > n:
        primes = primes[0:n]
        print(int(primes[-1]))    
        print("--- %s seconds ---" % (time.time() - start_time))
    else:
        v = h
        l = v
        h = 2*v
        primecounter_sieve(n, l, h, primes)


# In[128]:


#problem 8
num = 7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450

#convert num into a useable data type

num_arr = np.array([x for x in str(num)]).astype(int)

#print(type(num_arr))

#main script

max = 0
start_time = time.time() 

for i in range(0,len(num_arr)-13):
    #print(num_arr[i:i+13])
    sum = np.prod(num_arr[i:i+13])
    #print(sum)
    if sum > max:
        max = sum
        
print(max)
print("--- %s seconds ---" % (time.time() - start_time))
    


# In[138]:


#problem 9
import random
import time

start_time = time.time()

#generating Pythagorean tripples. 
tripples = []
for n in range(1,100):
    for m in range(n+1,100):
        if np.gcd(m,n) == 1 and m % 2 == 0 or n % 2 == 0:
            for k in range(1,100):
                x = k*(m*m-n*n)
                y = k*(2*m*n)
                z = k*(m*m + n*n)
                if x+y+z <= 1000:
                    tripples.append([x,y,z, x+y+z])

#finding the right tripple
for i in tripples:
    if i[-1] == 1000:
        print(i)
        print(i[0]*i[1]*i[2])
        
print('--- %s seconds ---' % (time.time() - start_time))
        
#testing random tripples:
#tripple = tripples[random.randint(0,len(tripples))]
#print(tripple)
#print(tripple[0]*tripple[0] + tripple[1]*tripple[1] == tripple[2]*tripple[2])

            


# In[356]:


#problem 10

#a better sieve
def sieve(n):
    time_start = time.time()
    integers = [[i,True] for i in range(2,n+1)]
    for p in range(2, int(math.sqrt(n))+1):
        if integers[p-2][1] == True:
            for k in range(2,n):
                if p*k - 2 < len(integers):
                    #print('p = ', p, 'k = ', k, 'number =', p*k, 'index =', p*k - 2)
                    integers[p*k - 2][1] = False
                    #print(integers)
    primes = [integers[i][0] for i in range(len(integers)) if integers[i][-1] == True]
    print('--- %s seconds ---' % (time.time() - time_start))
    return sum(primes)
    
sieve(2000000)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




