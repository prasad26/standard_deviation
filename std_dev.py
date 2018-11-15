from math import sqrt
import numpy as np
import matplotlib.pyplot as plt

def mean(lst):
    """calculates mean"""
    sum = 0
    for i in range(len(lst)):
        sum += lst[i]
    return (sum / len(lst))

def stddev(lst):
    """calculates standard deviation"""
    sum = 0
    mn = mean(lst)
    for i in range(len(lst)):
        sum += pow((lst[i]-mn),2)
    return sqrt(sum/len(lst)-1)

def variance(lst):
    sum = 0
    mn = mean(lst)
    for i in range(len(lst)):
        sum += pow((lst[i]-mn),2)
    return sum
	
numbers = range(100)

mu = mean(numbers)
sigma = stddev(numbers)
print(numbers)
print(mean(numbers))
print (stddev(numbers))
print (variance(numbers))

s = np.random.normal(mu, sigma, len(numbers))
count, bins, ignored = plt.hist(s, 10, density=True)
plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) * np.exp( - (bins - mu)**2 / (2 * sigma**2) ),linewidth=2, color='r')
plt.show()