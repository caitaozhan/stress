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
    if p.stderr.readlines():
        raise(f'error in run.py process:\n {p.stderr.readlines()}')

    for line in p.stdout:
        runtime = float(line[5:9])
        return runtime

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='stress the CPU')
    parser.add_argument('-t', '--tasks', type=int, nargs='+', default=[1, 2], help='number of tasks')
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
        print(f'# of task = {task}, runtimes = {runtimes}')

