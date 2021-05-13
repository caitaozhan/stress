'''
stress a single core with matrix multiplication
'''
import time
import numpy as np

if __name__ == '__main__':
    stop = int(1e7)
    start = time.time()
    for i in range(stop):            # time of one iteration is in the order of a few microseconds (10e-6 second)
        a = np.random.rand(10, 10)
        b = np.random.rand(10, 10)
        c = a@b
    print('time {:.2f}s'.format(time.time() - start))
