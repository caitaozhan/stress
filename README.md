# Introduction to CPU Performance Benchmark
It is interesting to see how the CPU advanced throughout the years. This repository is a simple performance benchmark, derived from my workflow that heavily uses Python and NumPy. 
Unlike other benchmarks, my benchmark's performance metric **has actual meanings**. The metric is the **runtime (in seconds) of completing some number of tasks concurrently**, and each task is fixed -- repeating $10\times10$ matrix multiplication $10^7$ times.

# How to Run the Benchmark
Stress a CPU by small matrix multiplication. I observe that **small matrix multiplication in NumPy only uses a single core**. Before running the benchmark, please close most, if not all, of your existing programs. To start the benchmark, please run the following in the terminal:
```
python stress.py -t 1 2 4 6 8 12 16
```
`-t` is short for `--tasks`, denoting the number of tasks running concurrently. Also, remember to run the `htop` command to observe the stressing process.

# Impact of Software on the Benchmark
For a CPU performance benchmark, we hope that software (i.e., operating systems and Python versions) shall have a minimal effect. Or else, we don't know whether the improvement is caused by hardware or software.
- *Operating System*. Linux is apparently faster than Windows (Windows performance is also strange, and varies a lot across different power modes). 
Microsoft put Linux inside Windows and created Windows Subsystems for Linux (WSL). 
The WSL 2 is faster than Windows. 
MacOS performance should be similar to Linux.

- *Python version*. [Python 3.11](https://github.com/caitaozhan/stress/blob/8a399b5a8d62d5beee7fbc3dcf75bed97d2c805b/results#L214) is around *14% faster* than [Python 3.8](https://github.com/caitaozhan/stress/blob/8a399b5a8d62d5beee7fbc3dcf75bed97d2c805b/results#L203) based on my benchmark running on my Macbook Pro (2021).
The difference is larger than I expected since my benchmark's bottleneck is running numpy.dot(), which is implemented in C/C++.

# Results

<p align="center">
  <picture>
   <img src="cpu_perf.png" width="700" class="center">
  </picture>
</p>

CPU performance is improving year by year. Currently, the best CPU tested is the M4 Max (12+4).
The complete raw data is [here](results). The oldest data point is from a MacBook Pro (Retina, 15-inch, Mid 2012).

# How to Contribute

1. Fork this repository to your GitHub.
2. git clone your forked repository.
3. Run `python stress.py -t 1 2 4 6 8 12 16` in the terminal. You can run `htop` command to see the stressing process. Also, please close your other applications if possible (so that the CPU resource is fully allocated to the stressing). Below is an example output:
```
# of tasks = 1, runtimes = [17.58]
# of tasks = 2, runtimes = [17.83, 18.09]
# of tasks = 4, runtimes = [19.1, 19.21, 19.31, 19.51]
# of tasks = 6, runtimes = [24.78, 25.0, 25.07, 25.08, 25.17, 25.47]
# of tasks = 8, runtimes = [29.37, 29.6, 29.65, 29.66, 29.65, 29.79, 30.03, 30.6]
# of tasks = 12, runtimes = [44.43, 44.54, 44.52, 44.67, 44.69, 44.73, 44.7, 44.74, 44.81, 44.87, 44.87, 44.97]
# of tasks = 16, runtimes = [60.9, 61.23, 61.27, 61.51, 61.43, 61.51, 61.55, 61.62, 61.63, 61.53, 61.76, 61.79, 61.73, 61.79, 61.72, 62.06]
```
4. Update the [result](results) file. Only pick the last (largest) number of each `runtimes` list. Also, please include meta including the CPU name, year of CPU, Python version, Opearting system name (no need for MacBook), number of performance and efficient cores. Below is an example.
```
MacBook Air (2022), Py 3.12
M2 (4 performance cores + 4 efficient cores)
Task | time(s)
1    | 17.58
2    | 18.09
4    | 19.51
6    | 25.47
8    | 30.6
12   | 44.97
16   | 62.06
```
5. Git add, commit, push.
6. Do a pull request.