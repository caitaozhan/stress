'''
Stress the RAM by copy.deepcopy
Stress the I/O by np.save
'''

import copy
import numpy as np
import time

if __name__ == '__main__':
    # test RAM
    object = np.random.rand(1024, 1024, 128)
    print(f'Size of object {object.nbytes / 1024**3:0.3f} GB')
    start = time.time()
    for _ in range(100):
        object2 = copy.deepcopy(object)
        del object2
    print(f'Time of deep copy a 1 GB object 100 times and deleting it = {time.time() - start:0.2f}s')
