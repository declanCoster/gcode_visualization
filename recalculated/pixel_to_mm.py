import os
import pandas as pd

df = pd.read_csv(os.path.join('..', 'cropped', 'corrected_location.csv'))
new_df = pd.DataFrame(columns=['0', '1', '2', '3', '4', '5'])
pixel_X = df['X'].to_list()
pixel_Y = df['Y'].to_list()

squ_err = 0

for i in range(len(pixel_X)):
    mm_X = 140 - (120/799)*pixel_X[i]
    mm_Y = 120 - (120/799)*pixel_Y[i]
    exp_X = round(mm_X/10)*10
    exp_Y = round(mm_Y/10)*10
    delta_X = exp_X - mm_X
    delta_Y = exp_Y - mm_Y
    squ_err += delta_Y**2 + delta_X**2
    new_df = new_df.append({'0': mm_X, '1': mm_Y, '2': exp_X, '3': exp_Y, '4': delta_X, '5': delta_Y}, ignore_index=True)

rmse = (squ_err/121)**.5
print(rmse)
new_df.to_csv(os.path.join('.', 'nn_correct_locations.csv'), index=False)
