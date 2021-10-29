'''
Stress the RAM  by copy.deepcopy
Stress the disk by np.save
'''

import copy
import numpy as np
import time
import shutil

def test_ram():
    object = np.random.rand(1024, 1024, 128)
    print(f'Size of object = {object.nbytes / 1024**3:0.3f} GB')
    start = time.time()
    for _ in range(100):
        object2 = copy.deepcopy(object)
        del object2
    print(f'Time of deep copying an 1 GB object 100 times and deleting it = {time.time() - start:0.2f}s')

def test_disk():
    object = np.random.rand(1024, 1024, 128)
    print(f'Size of object = {object.nbytes / 1024**3:0.3f} GB')
    filename = 'object.npy'
    start = time.time()
    for _ in range(20):
        np.save(filename, object)
    print(f'Time of writing an 1 GB object 20 times = {time.time() - start:0.3f}s')
    
    start = time.time()
    for _ in range(20):
        object = np.load(filename)
    print(f'Time of reading an 1 GB object 20 times = {time.time() - start:0.3f}s')


if __name__ == '__main__':
    # test_ram()
    test_disk()
