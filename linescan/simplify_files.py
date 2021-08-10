import os
import re
import glob 
import natsort
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import minmax_scale
# from this repo:
from functions.utils import get_files

data_dir = os.path.abspath('../data/210319_linescans')
print(data_dir)
data_folders = get_files(data_dir + '/*')
out_dir = os.path.abspath('../data/simplified_heatmap_data')

for folder in data_folders:
    folder_name = folder.split('/')[-1]
    new_path = os.path.join(out_dir, folder_name)
    datasets = get_files(folder + '/*.csv')
    if not os.path.exists(new_path):
        os.makedirs(new_path)
    
    # divide into color channels:
    cyan_data = [val for val in datasets if re.search(r'cyan\.csv', val)]
    yellow_data = [val for val in datasets if re.search(r'yellow\.csv', val)]
    magenta_data = [val for val in datasets if re.search(r'(mag|magenta)\.csv', val)]
    # sanity check to make sure they are the same number of files
    assert len(cyan_data)==len(yellow_data)==len(magenta_data)
    print('There are {} files of each color'.format(len(cyan_data)))

    # only want file names to extract naming convention
    cyan_filenames = [val.split('/')[-1] for val in cyan_data]
    yellow_filenames = [val.split('/')[-1] for val in yellow_data]
    magenta_filenames = [val.split('/')[-1] for val in magenta_data]
    # regex pattern:
    pattern = re.compile("_(\d*)_(\d*)_\d*_\w*\.csv")

    ## For each color channel:
    uniq_cyan = []
    uniq_yellow = []
    uniq_magenta = []

    ## Find unique regex matches:
    for names in cyan_filenames:
        name_set = [pattern.search(names).group(1), pattern.search(names).group(2)]
        if name_set not in uniq_cyan:
            uniq_cyan.append(name_set)

    for names in yellow_filenames:
        name_set = [pattern.search(names).group(1), pattern.search(names).group(2)]
        if name_set not in uniq_yellow:
            uniq_yellow.append(name_set)
    
    for names in magenta_filenames:
        name_set = [pattern.search(names).group(1), pattern.search(names).group(2)]
        if name_set not in uniq_magenta:
            uniq_magenta.append(name_set)

    ## New Glob to get cyan ref-frame specific datasets:
    for combo in uniq_cyan:
        pattern = folder + '/_' + combo[0] + '_' + combo[1] + '_*_cyan.csv'
        matches = get_files(pattern)

        # extract frame #'s as column labels:
        clabels = []
        for path in matches:
            clabels.append(path.split('/')[-1].split('_')[3])
        # create dataframe
        df = pd.concat((pd.read_csv(f, usecols=['Value']) for f in matches), axis = 1).fillna(0)
        df.columns = clabels
        # save dataframe
        df.to_csv(new_path + '/mod-' + combo[0] + '_ref-' + combo[1] + '_cyan.csv', index=False)

    # yelllow
    for combo in uniq_yellow:
        pattern = folder + '/_' + combo[0] + '_' + combo[1] + '_*_yellow.csv'
        matches = get_files(pattern)

        # extract frame #'s as column labels:
        clabels = []
        for path in matches:
            clabels.append(path.split('/')[-1].split('_')[3])
        # create dataframe
        df = pd.concat((pd.read_csv(f, usecols=['Value']) for f in matches), axis = 1).fillna(0)
        df.columns = clabels
        # save dataframe
        df.to_csv(new_path + '/mod-' + combo[0] + '_ref-' + combo[1] + '_yellow.csv', index=False)

    # magenta
    for combo in uniq_magenta:
        pattern = folder + '/_' + combo[0] + '_' + combo[1] + '_*_magenta.csv'
        matches = get_files(pattern)

        # extract frame #'s as column labels:
        clabels = []
        for path in matches:
            clabels.append(path.split('/')[-1].split('_')[3])
        # create dataframe
        df = pd.concat((pd.read_csv(f, usecols=['Value']) for f in matches), axis = 1).fillna(0)
        df.columns = clabels
        # save dataframe
        df.to_csv(new_path + '/mod-' + combo[0] + '_ref-' + combo[1] + '_magenta.csv', index=False)