# Introduction
This is a simple and naive performance testing tool, derived from my workflow (need python3 and numpy). The testing is not comprehensive, but I think it is a good enough estimation.

# Test CPU Performance
Stress all kinds of CPU mainly by matrix multiplication. Just run the following in the terminal:

**python3 stress.py -t 1 2 4 6 8 12 16**

# Results
Summary: M1 Pro is a laptop CPU (red line), but it beats the high-end desktop Intel CPU (green line), not to mention the labtop Intel CPU (blue and orange line).
Most laptop CPU are bad at maintaining the frequency when the number of tasks（one task is doing 10x10 matrix multiplication 10 million times）increase, i.e. frequency will drop. The M1 Pro is an exception.

![cpu_perf](https://github.com/caitaozhan/stress/blob/main/cpu_perf.png)
