'''
stress a single core with a lot of matrix multiplications

10/27/2021: 
Note that the Apple built-in python2 and python3 are directly running on the Apple silicon,
whereas the Anaconda's python2 and python3 has to go through the rosetta, almost doubling the runtime.

7/25/2022:
When evaluating Python on Apple Sillicon, need to be careful that your Anaconda might be running on Rosetta
(increase runtime nearly by a factor of 2). Prior April 2022, the Anaconda only has intel version. 
To circumvent Rosetta, need to use the MacOS's built-in Python3. After May 2022, Anaconda released the M1 chip version
and it is as fast the MacOS's built-in Python3.


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
