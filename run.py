'''
stress a single core with a lot of matrix multiplications

10/27/2021: Note that the Apple built-in python2 and python3 are directly running on the Apple silicon,
whereas the Anaconda's python2 and python3 has to go through the rosetta, almost doubling the runtime.
'''

import time
import numpy as np

if __name__ == '__main__':
    repeat = int(1e6)
    start = time.time()
    for i in range(repeat):
        a = np.random.rand(10, 10)
        b = np.random.rand(10, 10)
        c = np.dot(a,b)
    print('time={:.2f}s'.format(time.time() - start))
