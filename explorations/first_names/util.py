import pandas as pd
import numpy as np
import glob 
import os
import sys


def load_stitch_files(folder_path, col_names, filetype="csv", year_from_filename=True):
    """ find all files of this type in this folder, 
    and return them all in a single df
    """
    filepaths = glob.glob('{}/*.{}'.format(folder_path, filetype)) 
    df_list = []
    if year_from_filename:
        final_df = pd.concat(
            [
                pd.read_csv(f, header=None, names=col_names)
                    .assign(year=int(f[-8:-4])) # get year from filename
                for f in filepaths
            ],
            ignore_index=True
        )
    else: # TODO: don't duplicate code
        final_df = pd.concat(
            [
                pd.read_csv(f, header=None, names=col_names)
                for f in filepaths
            ],
            ignore_index=True
        )
    return final_df

