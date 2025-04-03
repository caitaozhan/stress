import matplotlib.pyplot as plt
import numpy as np

def plot():
    X  = [1,    2,    4,    6,    8,    12,   16]
    y1 = [40,   42,   52,   70,   92]                # i5-1038NG7
    y2 = [33,   35,   35,   35,   35,   51,   64]    # i7-10700KF
    y3 = [23,   24,   24,   25,   30,   44,   60]    # M1 Pro (6 + 2)
    y4 = [19,   19,   22,   26,   33,   47,   65]    # M2 (4 + 4)
    y5 = [17,   17,   17,   18,   18,   24,   32]    # i7-13700K (8 + 8)
    y6 = [15.6, 15.9, 16.8, 19.2, 22.2, 29.0, 37.6]  # M3 Pro (6 + 5)
    y7 = [20.1, 22.1, 22.3, 22.3, 22.3, 23.6, 23.6]  # Ryzen 9 7950X3D (16)
    y8 = [13.2, 14.0, 14.5, 14.5, 14.9, 18.5, 23.5]  # M4 Pro (10 + 4)
    y9 = [11.8, 12.5, 13.3, 13.0, 13.5, 14.8, 18.2]  # M4 MAx (12 + 4)

    plt.rcParams['font.size'] = 45
    plt.rcParams['lines.linewidth'] = 9
    fig, ax = plt.subplots(1, 1, figsize=(28, 26))
    fig.subplots_adjust(left=0.08, right=0.99, top=0.845, bottom=0.09)
    ax.plot(np.arange(len(y1)), y1, marker='o', markersize=20, label='i5-1038NG7, 4 (MBP, 2020)')
    ax.plot(np.arange(len(y2)), y2, marker='o', markersize=20, label='i7-10700KF, 8 (ABS, 2021, Ubuntu, Py3.9)')
    ax.plot(np.arange(len(y3)), y3, marker='o', markersize=20, label='M1 Pro, 6+2 (MBP, 2021, Py3.8)')
    ax.plot(np.arange(len(y7)), y7, marker='o', markersize=20, label='Ryzen 9 7950X3D, 16 (2024, Ubuntu, Py3.12)')
    ax.plot(np.arange(len(y4)), y4, marker='o', markersize=20, label='M2, 4+4 (MBA, 2022, Py3.10)')
    ax.plot(np.arange(len(y5)), y5, marker='o', markersize=20, label='i7-13700K, 8+8 (2023, WSL2, Py3.10)')
    ax.plot(np.arange(len(y6)), y6, marker='o', markersize=20, label='M3 Pro, 5+6 (MBP, 2023, Py3.12)')
    ax.plot(np.arange(len(y8)), y8, marker='o', markersize=20, label='M4 Pro, 10+4 (MBP, 2024, Py3.12)')
    ax.plot(np.arange(len(y9)), y9, marker='o', markersize=20, label='M4 Max, 12+4 (MBP, 2024, Py3.11)')
    fig.legend(ncol=2, fontsize=36, bbox_to_anchor=(0.99, 1.005))
    ax.grid()
    ax.set_xlim([-0.05, 6.05])
    ax.set_xticks(np.arange(len(X)))
    ax.set_xticklabels([str(x) for x in X])
    ax.set_xlabel('Number of Concurrent Tasks\n(task = do 10x10 matrix multiplication $10^7$ times)')
    ax.set_ylabel('Runtime (s)', fontsize=50, labelpad=20)
    ax.set_ylim([0, 93])
    y_ticks = list(range(0, 100, 10))
    ax.set_yticks(y_ticks)
    ax.tick_params(axis='x', direction='in', length=10, width=3, pad=15)
    ax.tick_params(axis='y', direction='in', length=10, width=3, pad=15)
    fig.savefig('cpu_perf.png')


if __name__ == '__main__':
    plot()
