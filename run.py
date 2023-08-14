'''
stress a single core with a small matrix multiplications. Small matrix multiplication in Numpy uses single core, while large matrix multiplicaiton in Numpy uses multi-core.

10/27/2021: 
Note that the Apple built-in python2 and python3 are directly running on the Apple silicon,
whereas the Anaconda's python2 and python3 has to go through the rosetta, almost doubling the runtime.

Sep. 2021: Realized that Anaconda has released a version for Apple Silicon on May 2022.

'''

import time
import numpy as np

if __name__ == '__main__':
    repeat = int(1e7)
    start = time.time()
    for i in range(repeat):
        a = np.random.rand(10, 10)
        b = np.random.rand(10, 10)
        c = np.dot(a,b)
    print('time={:.2f}s'.format(time.time() - start))
