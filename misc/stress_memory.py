'''
My own simple version of testing RAM and disk based on my workflow.
Stress the RAM  by copy.deepcopy
Stress the disk by np.save and np.load

For more comprehensive testing: https://fio.readthedocs.io/en/latest/fio_doc.html
'''

import copy
import numpy as np
import time
import os

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
    def helper(object, repeat):
        size_gb = object.nbytes / 1024**3
        filename = 'object-{}.npy'

        start = time.time()
        for i in range(repeat):
            np.save(filename.format(i), object)
        elapse = time.time() - start
        print(f'Time of writing a {size_gb:.6f} GB object {repeat:>4} times       = {elapse:0.2f}s, speed = {size_gb*repeat/elapse:0.2f} GB/s')
        del object

        start = time.time()
        objects = []
        for i in range(repeat):
            objects.append(np.load(filename.format(i)))
        elapse = time.time() - start
        print(f'Time of reading a {size_gb:.6f} GB object {repeat:>4} times       = {elapse:0.2f}s, speed = {size_gb*repeat/elapse:0.2f} GB/s')

        # delete the files for testing
        for i in range(repeat):
            os.remove(filename.format(i))

    object = np.random.rand(1024, 131)
    repeat = 5000
    helper(object, repeat)
    object = np.random.rand(1024, 1311, 1)
    repeat = 500
    helper(object, repeat)
    object = np.random.rand(1024, 1024, 128)
    repeat = 5
    helper(object, repeat)



if __name__ == '__main__':
    test_ram()
    # test_disk()
