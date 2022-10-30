import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def dtw(s, t):
    n, m = len(s), len(t)
    dtw_matrix = np.zeros((n+1, m+1))
    for i in range(n+1):
        for j in range(m+1):
            dtw_matrix[i, j] = np.inf
    dtw_matrix[0, 0] = 0
    
    for i in range(1, n+1):
        for j in range(1, m+1):
            cost = abs(s[i-1] - t[j-1])
            last_min = np.min([dtw_matrix[i-1, j], dtw_matrix[i, j-1], dtw_matrix[i-1, j-1]])
            dtw_matrix[i, j] = cost + last_min
    return dtw_matrix[n][m]

sitting = pd.read_csv('sitting.csv', header=None)
sitting_ax = sitting[3]
sitting_ay = sitting[4]
sitting_az = sitting[5]

standing = pd.read_csv('standing.csv', header=None)
standing_ax = standing[3]
standing_ay = standing[4]
standing_az = standing[5]

sleeping = pd.read_csv('sleeping.csv', header=None)
sleeping_ax = sleeping[3]
sleeping_ay = sleeping[4]
sleeping_az = sleeping[5]

def animate(i):
    data = pd.read_csv('data.csv', header=None)
    t = data[2]
    ax = data[3]
    ay = data[4]
    az = data[5]

    dtw_sitting_x, dtw_sitting_y, dtw_sitting_z = dtw(ax,sitting_ax), dtw(ay,sitting_ay), dtw(az,sitting_az)
    dtw_standing_x, dtw_standing_y, dtw_standing_z = dtw(ax,standing_ax), dtw(ay,standing_ay), dtw(az,standing_az)
    dtw_sleeping_x, dtw_sleeping_y, dtw_sleeping_z = dtw(ax,sleeping_ax), dtw(ay,sleeping_ay), dtw(az,sleeping_az)

    plt.cla()

    plt.xlabel("t")
    plt.ylabel("a")
    plt.plot(t, ax, label='x')
    plt.plot(t, ay, label='y')
    plt.plot(t, az, label='z')
    plt.grid()

    if((np.min([dtw_sitting_x, dtw_standing_x, dtw_sleeping_x]) == dtw_sitting_x) and (np.min([dtw_sitting_y, dtw_standing_y, dtw_sleeping_y]) == dtw_sitting_y) and (np.min([dtw_sitting_z, dtw_standing_z, dtw_sleeping_z]) == dtw_sitting_z)):
        plt.title("SITTING")
    elif((np.min([dtw_sitting_x, dtw_standing_x, dtw_sleeping_x]) == dtw_standing_x) and (np.min([dtw_sitting_y, dtw_standing_y, dtw_sleeping_y]) == dtw_standing_y) and (np.min([dtw_sitting_z, dtw_standing_z, dtw_sleeping_z]) == dtw_standing_z)):
        plt.title("STANDING")
    elif((np.min([dtw_sitting_x, dtw_standing_x, dtw_sleeping_x]) == dtw_sleeping_x) and (np.min([dtw_sitting_y, dtw_standing_y, dtw_sleeping_y]) == dtw_sleeping_y) and (np.min([dtw_sitting_z, dtw_standing_z, dtw_sleeping_z]) == dtw_sleeping_z)):
        plt.title("SLEEPING")


    plt.legend(loc='upper left')


ani = FuncAnimation(plt.gcf(), animate, interval=100)

plt.show()