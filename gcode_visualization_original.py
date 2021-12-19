import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.figure(figsize=(10,10))

plt.gca().invert_yaxis()
# plt.gca().invert_xaxis()
img = plt.imread(os.path.join('.', 'cropped', 'original.png'))
plt.imshow(img, extent=[140, 20, 0, 120])
### Plot Edge Corners
# plt.imshow(img, extent=[20, 140, 0, 120])
# plt.gca().invert_yaxis()
plt.scatter([20, 140, 20, 140], [0, 0, 120, 120], c='b')
# fig, ax = plt.subplots()

### Ploting Observed Points
df = pd.read_csv(os.path.join('.', 'csv', 'uncorrected_regular.csv'))
X_obs = df['0'].to_list()
Y_obs = df['1'].to_list()
plt.scatter(X_obs, Y_obs, c='#FFA500')
# print(X_obs[0])
# print(Y_obs[0])

### Plot Lines of Gcode File
Xprev = None
Yprev = None
gcode_file = 'gcode_files/1.gcode'
with open(gcode_file) as fp:
    for line_text in fp.readlines():
        line_list = line_text.split(' ')
        draw_mode = False
        X = None
        Y = None
        for line_part in line_list:
            if line_part == 'G1' or line_part == 'G01':
                draw_mode = True
            if 'X' in line_part:
                X = float(line_part[1:])
            if 'Y' in line_part:
                Y = float(line_part[1:])
        if draw_mode and X and Y and Xprev and Yprev:
            plt.plot([Xprev, X], [Yprev, Y], 'b')
        Xprev = X
        Yprev = Y

plt.savefig('cropped/original_perfect_and_points.png', transparent=False)

Xprev = None
Yprev = None
gcode_file = 'gcode_files/nn_corrected_1.gcode'
with open(gcode_file) as fp:
    for line_text in fp.readlines():
        line_list = line_text.split(' ')
        draw_mode = False
        X = None
        Y = None
        for line_part in line_list:
            if line_part == 'G1' or line_part == 'G01':
                draw_mode = True
            if 'X' in line_part:
                X = float(line_part[1:])
            if 'Y' in line_part:
                Y = float(line_part[1:])
        if draw_mode and X and Y and Xprev and Yprev:
            plt.plot([Xprev, X], [Yprev, Y], 'r')
        Xprev = X
        Yprev = Y


### Save Figure
# plt.savefig(gcode_file[:(len(gcode_file)-6)] + '.png')
plt.savefig('cropped/original_points.png', transparent=False)

df_corrected = pd.read_csv(os.path.join('.', 'csv', 'nn_regular.csv'))
X_cor = df_corrected['0'].to_list()
Y_cor = df_corrected['1'].to_list()
# U = np.array(X_cor) - np.array(X_obs)
# V = np.array(Y_cor) - np.array(Y_obs)
X = np.zeros((11,11))
Y = np.zeros((11,11))
U = np.zeros((11,11))
V = np.zeros((11,11))
for i in range(len(X_cor)):
    fst = i//11
    snd = i % 11
    X[fst, snd] = X_obs[i]
    Y[fst, snd] = Y_obs[i]
    U[fst, snd] = X_cor[i] - X_obs[i]
    V[fst, snd] = Y_cor[i] - Y_obs[i]
    plt.arrow(X[fst, snd], Y[fst, snd], U[fst, snd], V[fst, snd])
### Quiver
# plt.quiver([X, Y], U, V)

plt.savefig('cropped/original_quiver.png', transparent=False)

