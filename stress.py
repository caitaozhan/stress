'''
stress the CPU
'''

import argparse
import subprocess
import time
from subprocess import Popen

def get_runtime(p: Popen):
    '''get the stdout and extract the runtime
       example stdout: b'time=2.33s\n'
    '''
    error = p.stderr.readlines()
    if error:
        for line in error:
            print(line)
        raise('error in run.py process')

    for line in p.stdout:
        line = line.decode('ASCII')  # b'time=23.33s\n' --> 'time=23.33s\n'
        s = line.find('=')
        e = line.find('s')
        runtime = float(line[s+1:e])
        return runtime

# example: python3 stress.py -t 1 2 4 8

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='stress the CPU')
    parser.add_argument('-t', '--tasks', type=int, nargs='+', default=[1, 2, 4, 6, 8], help='number of tasks')
    args = parser.parse_args()

    for task in args.tasks:
        # run the tasks
        ps = []
        for i in range(task):
            command = ['python', 'run.py']
            ps.append(Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE))
        
        # wait for the tasks to finish and get each task's runtime
        runtimes = []
        while len(ps) > 0:
            new_ps = []
            for p in ps:
                if p.poll() is None:
                    new_ps.append(p)
                else:
                    runtimes.append(get_runtime(p))
            ps = new_ps
            time.sleep(1)
        print(f'# of tasks = {task}, runtimes = {runtimes}')
        
        # a little rest
        time.sleep(3)

