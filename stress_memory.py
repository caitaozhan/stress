'''
My own simple version of testing RAM and disk based on my workflow.
Stress the RAM  by copy.deepcopy
Stress the disk by np.save and np.load

For more comprehensive testing: https://fio.readthedocs.io/en/latest/fio_doc.html
'''

import copy
import numpy as np
import time

def test_ram():
    print('=== Test RAM ===')
    object = np.random.rand(1024, 1024, 128)
    size_gb = object.nbytes / 1024**3
    start = time.time()
    for _ in range(100):
        object2 = copy.deepcopy(object)
        del object2   # manual delete will slightly decrease the time
    elapse = time.time() - start
    print(f'Time of deep copying a {size_gb} GB object 100 times = {elapse:0.2f}s, speed = {100/elapse:0.2f} GB/s')

def test_disk():
    print('=== Test Disk ===')
    object = np.random.rand(1024, 1024, 128)
    size_gb = object.nbytes / 1024**3
    filename = 'object.npy'

    start = time.time()
    for _ in range(10):
        np.save(filename, object)
    elapse = time.time() - start
    print(f'Time of writing a {size_gb} GB object 10 times       = {elapse:0.2f}s, speed = {10/elapse:0.2f} GB/s')
    
    start = time.time()
    for _ in range(10):
        object = np.load(filename)
        del object
    elapse = time.time() - start
    print(f'Time of reading a {size_gb} GB object 10 times       = {elapse:0.2f}s, speed = {10/elapse:0.2f} GB/s')


if __name__ == '__main__':
    test_ram()
    test_disk()
