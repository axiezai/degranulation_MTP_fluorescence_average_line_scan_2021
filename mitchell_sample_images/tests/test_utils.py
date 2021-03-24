import numpy as np 
import pandas as pd

from ..functions.utils import find_middle, realign_data, shift_data

def test_find_middle_odd():
    # test if a given odd length array returns the right index
    test_array = np.arange(9)
    mid = 4
    output = find_middle(test_array)
    assert output == mid


def test_find_middle_even():
    # test if a given even array returns the right index
    test_array = np.arange(12)  # 12 length long array
    mid = 6
    output = find_middle(test_array)
    assert output == mid


def test_realign_data_max():
    d1 = np.arange(9)
    d2 = np.arange(6)
    d1 = d1 * d1[::-1]
    d2 = d2 * d2[::-1]
    true_shift = np.array([0, 2])
    test_df = pd.DataFrame([d1, d2]).fillna(0)
    test_df = test_df.T
    d, shifts = realign_data(test_df)
    np.testing.assert_array_equal(true_shift, shifts)


def test_shift_data():
    d1 = np.arange(9)
    d2 = np.arange(6)
    d1 = d1 * d1[::-1]
    d2 = d2 * d2[::-1]
    true_shift = np.array([0, 2])
    test_df = pd.DataFrame([d1, d2]).fillna(0)
    test_df = test_df.T
    d_out = shift_data(test_df, true_shift)
    np.testing.assert_array_equal(d_out.iloc[:,0], test_df.iloc[:,0])
    assert test_df.iloc[3,1] == d_out.iloc[3+true_shift[1],1]