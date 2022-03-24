from absl import app
from absl import flags

import poisson

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
    print('benchmarking time for generating symmetric skellam..... ')
    while test_index < num_runs:
        start = time.time()

        samples = [poisson.PoissonInt(mx,my) for i in range(size)]
        samples = [samples_1[i]-samples_1[i+size] for i in range(size)]

        end = time.time()
        elapsed_time = end - start
        print('generated ', size, ' samples in ', elapsed_time, ' seconds.' )
        overall_time = overall_time + elapsed_time
        test_index = test_index + 1

    print('On average, generated ', size, ' samples in ', overall_time/num_runs, ' seconds.' )

if __name__ == '__main__':
    app.run(main)
