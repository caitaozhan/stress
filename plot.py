import matplotlib.pyplot as plt
import numpy as np

def plot():
    X  = [1,    2,    4,    6,    8,    12,   16]
    y1 = [40,   42,   52,   70,   92]                # i5-1038NG7
    y2 = [44,   44,   54,   83,   121]               # i7-1065G7
    y3 = [33,   35,   35,   35,   35,   51,   64]    # i7-10700KF
    y4 = [23,   24,   24,   25,   30,   44,   60]    # M1 Pro (6 + 2)
    y5 = [19,   19,   22,   26,   33,   47,   65]    # M2 (4 + 4)
    y6 = [17,   17,   17,   18,   18,   24,   32]    # i7-13700K (8 + 8)
    y7 = [15.6, 15.9, 16.8, 19.2, 22.2, 29.0, 37.6]  # M3 Pro (6 + 5)

    plt.rcParams['font.size'] = 45
    plt.rcParams['lines.linewidth'] = 10
    fig, ax = plt.subplots(1, 1, figsize=(20, 24))
    fig.subplots_adjust(left=0.15, right=0.95, top=0.77, bottom=0.1)
    # ax.plot(np.arange(len(y2)), y2, marker='o', markersize=20, label='i7-1065G7 (Microsoft Surface 3 2020)')
    ax.plot(np.arange(len(y1)), y1, marker='o', markersize=20, label='i5-1038NG7 (MacBook Pro, 2020)')
    ax.plot(np.arange(len(y3)), y3, marker='o', markersize=20, label='i7-10700KF (ABS Legend Gaming, 2021, Ubuntu, Py 3.9)')
    ax.plot(np.arange(len(y4)), y4, marker='o', markersize=20, label='M1 Pro 6+2 core (MacBook Pro, 2021, Py 3.8)')
    ax.plot(np.arange(len(y5)), y5, marker='o', markersize=20, label='M2 4+4 core (MacBook Air, 2022)')
    ax.plot(np.arange(len(y6)), y6, marker='o', markersize=20, label='i7-13700K (Custom Built Desktop, 2023, WSL 2, Py 3.10)')
    ax.plot(np.arange(len(y7)), y7, marker='o', markersize=20, label='M3 Pro 6+5 core (MacBook Pro, 2023, 3.12)')
    fig.legend(ncol=1, fontsize=40, bbox_to_anchor=(0.97, 1.01))
    ax.grid()
    ax.set_xticks(np.arange(len(X)))
    ax.set_xticklabels([str(x) for x in X])
    ax.set_xlabel('Number of Concurrent Tasks\n(task = do 10x10 matrix multiplication $10^7$ times)')
    ax.set_ylabel('Runtime (s)', fontsize=50)
    ax.set_ylim([0, 100])
    y_ticks = list(range(0, 110, 10))
    ax.set_yticks(y_ticks)
    ax.tick_params(axis='x', direction='in', length=10, width=3, pad=15)
    ax.tick_params(axis='y', direction='in', length=10, width=3, pad=15)
    fig.savefig('cpu_perf.png')


if __name__ == '__main__':
    plot()
