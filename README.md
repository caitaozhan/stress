# Introduction
It is interesting to see how the CPU advances throughout the years. This repository is a simple performance benchmark, derived from my workflow that heavily uses Python3 and Numpy. 
Different than other benchmarks, my benchmark's performance metric **has actual meanings**. It is the **runtime** of doing a **fixed task** -- repeat $10\times10$ matrix multiplication $10^7$ times.

# My CPU Performance Benchmark
Stress a CPU by small matrix multiplication (I observe that small matrix multipliaction in Numpy only uses a single core, while large matrix multiplication may use multi-core). To start the benchmark, please run the following in the terminal:

**python stress.py -t 1 2 4 6 8 12 16**

# How Software Impact the Perforamnce
- Operating System has an impact on the performance. Linux is apparently faster than Windows (Windows performance is also strange, and varies a lot accross different power modes). Microsoft smartly put a Linux inside the Windows and created Windows Subsystems for Linux (WSL). The WSL 2 is faster than Windows. MacOS performance should be similar to Linux.

- Python version does impact the performance. I have tested that Python 3.11 is a little over *10% faster* than 3.8 based on my benchmark. The difference is larger than I expected, since my benchmark's bottleneck is running numpy.dot(), which is implemented in C, and C should rarely change through out the years. When newer Python verison come out, I do not rerun the old results because very often the results were ran on other people's computer, so it is inconvenient to rerun. 

# Results

![cpu_perf](cpu_perf.png)

**Evaluation**
1. Intel has finally significantly improved in recent years. The 13th gen (purple line) desktop CPU is a lot faster than then 10th gen (orange line).
2. M1 Pro is a laptop CPU (green line), but it beats the high-end desktop Intel CPU (orange line), not to mention the labtop 10th-gen Intel CPU (blue line). 
3. M2 in MacBook Air (red line) is faster than M1 Pro (green line) when the number of task is 4 or under, but is slower when the number of task is larger than 4. This is because the M1 Pro has 6 performance cores and 2 efficiency cores while the M2 has 4 performance cores and 4 efficiency cores.


**More**: The complete raw data is [here](results). I have the data since the 3rd generation Intel chip using Ivy Bridge 22 nm microarchitecture. That was the laptop during my undergrad (2013~2017).