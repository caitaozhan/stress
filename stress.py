'''
stress the CPU
'''

from subprocess import Popen


if __name__ == '__main__':
    task = 4
    ps = []
    for i in range(task):
        command = ['python', 'run.py']
        p = Popen(command)

