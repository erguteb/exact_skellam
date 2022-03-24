import time
import random #Default random number generator

from absl import app
from absl import flags
FLAGS = flags.FLAGS
flags.DEFINE_integer('mx', 1, 'mx for poissonint')
flags.DEFINE_integer('my', 1, 'my for poisson int')
flags.DEFINE_integer('m', 1, 'number of runs')

#sample from a Bernoulli(px/py) distribution
#px, py are integers
def sample_bernoulli(px,py,rng):
    assert 0 <= px/py <= 1
    m = rng.randrange(py)
    if m < px:
        return 1
    else:
        return 0

# sample from Bernoulli
def BinomialInt(trials, px, py, rng):
    if trials < 0: return -1
    if trials == 0: return 0
    if px == 0: return 0
    if px == py: return trials
    r = 0
    for i in range(trials):
        if sample_bernoulli(px,py,rng) == 1:
            r = count + 1
    return count

def Poisson1(rng):
    ret = 1
    a = 1
    b = 0
    while True:
        j = rng.randrange(a)
        if j < a and j < b: return ret
        if j == a:
            ret = ret + 1
        else:
            ret = ret - 1
            b = a + 1
        a = a + 1

def PoissonInt(mx, my, rng=None):
    if rng is None:
        rng = random.SystemRandom()
    # sample from Poisson with lamabda = mx/my, mx,my are integers
    if my == 0: return -1 # error
    if mx == 0 or (mx < 0 and my < 0) or (mx > 0 and my < 0): return 0
    r = 0
    while mx >= my:
        r = r + Poisson1(rng)
        mx = mx-my
    if mx > 0:
        num = Poisson1(rng)
        r = r + BinomialInt(num, mx, my, rng)
    return r

def main(argv):
    del argv  # argv is not used.
    assert FLAGS.mx is not None, 'Flag mx is missing.'
    assert FLAGS.my is not None, 'Flag my is missing.'
    assert FLAGS.m is not None, 'Flag m is missing.'
    mx = FLAGS.mx
    my = FLAGS.my
    num_runs = FLAGS.m

    size = 10000
    test_index = 0
    overall_time = 0
    print('benchmarking time for generating poisson..... ')
    while test_index < num_runs:
        start = time.time()

        samples_1 = [PoissonInt(mx,my) for i in range(2*size)]
        samples = [samples_1[i]-samples_1[i+size] for i in range(size)]

        end = time.time()
        elapsed_time = end - start
        print('generated ', size, ' samples in ', elapsed_time, ' seconds.' )
        overall_time = overall_time + elapsed_time
        test_index = test_index + 1

    print('On average, generated ', size, ' samples in ', overall_time/num_runs, ' seconds.' )

if __name__ == '__main__':
    app.run(main)
