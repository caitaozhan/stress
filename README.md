# Stress
Stress all kinds of CPU by matrix multiplication (need numpy). Just run the following in the terminal:

**python3 stress.py -t 1 2 4 6 8 12 16**

# Results
Summary: M1 Pro is a laptop CPU (red line), but it beats the high-end desktop Intel CPU (green line), not to mention the labtop Intel CPU (blue and orange line).
Most laptop CPU are bad at maintaining the frequency when the number of tasks increase (frequency will drop). The M1 Pro is an exception.

![cpu_perf](https://github.com/caitaozhan/stress/blob/main/cpu_perf.png)
