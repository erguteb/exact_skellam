import time
import random #Default random number generator
import math
from scipy import stats

#sample from a Bernoulli(px/py) distribution
#px, py are integers
def sample_bernoulli(px,py,rng):
    assert 0 <= px/py <= 1
    m = rng.randrange(py)
    if m < px:
        return 1
    else:
        return 0

# sample from binomial(trials, px/py)
def BinomialInt(trials, px, py, rng):
    if trials < 0: return -1
    if trials == 0: return 0
    if px == 0: return 0
    if px == py: return trials
    r = 0
    for i in range(trials):
        if sample_bernoulli(px,py,rng) == 1:
            r = r + 1
    return r

# Algorithm 1 in Duchon and Duvignau, 2016.
def Poisson1(rng):
    n = 1
    g = 0
    k = 1
    while True:
        i = rng.randrange(n)
        if i == n + 1: k = k + 1
        elif i > g:
            k = k - 1
            g = n + 1
        else:
            return k
        n = n + 1

def PoissonInt(mx, my, rng=None):
    if rng is None:
        rng = random.SystemRandom()
    # sample from Poisson with lamabda = mx/my, mx,my are integers
    if my == 0: return -1 # error
    if mx == 0 or (mx < 0 and my < 0) or (mx > 0 and my < 0): return 0
    r = 0
    while mx >= my:
        # deduce the parameter by 1
        r = r + Poisson1(rng)
        mx = mx-my
    if mx > 0:
        # see page 487 in Devroye, 1986.
        num = Poisson1(rng)
        r = r + BinomialInt(num, mx, my, rng)
    return r

n = 100000
mx = 95
my = 3
print('benchmarking time for generating poisson..... ')
start = time.time()

samples = [PoissonInt(mx,my) for i in range(n)]

#now process
samples.sort()
values=[]
counts=[]
counter=None
prev=None
for sample in samples:
    if prev is None: #initializing
        prev=sample
        counter=1
    elif sample==prev: #still same element
        counter=counter+1
    else:
        #add prev to histogram
        values.append(prev)
        counts.append(counter)
        #start counting
        prev=sample
        counter=1
#add final value
values.append(prev)
counts.append(counter)

#print & sum
sum=0
sumsquared=0
kl=0
for i in range(len(values)):
    if len(values)<=100: #don't print too much
        print(str(values[i])+":\t"+str(counts[i]))
    sum = sum + values[i]*counts[i]
    sumsquared = sumsquared + values[i]*values[i]*counts[i]
    kl = kl + counts[i]*(math.log(counts[i]/n)-stats.poisson.logpmf(values[i], mx/my))
mean = sum/n
var = sumsquared/n
kl = kl/n
true_mean = mx/my
true_var = mx/my
print("mean="+str(float(mean))+" (true="+str(true_mean)+")")
print("variance="+str(float(var))+" (true="+str(true_var)+")")
print("KL(empirical||true)="+str(kl))
