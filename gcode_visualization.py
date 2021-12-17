import os
import numpy as np
import matplotlib.pyplot as plt
plt.figure(figsize=(10,10))
plt.gca().invert_yaxis()

img = plt.imread(os.path.join('.', 'cropped', 'original.png'))
### Plot Edge Corners
plt.imshow(img, extent=[20, 140, 0, 120])
plt.scatter([20, 140, 20, 140], [0, 0, 120, 120], c='b')
# fig, ax = plt.subplots()

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
plt.savefig('cropped/original.png', transparent=False)

