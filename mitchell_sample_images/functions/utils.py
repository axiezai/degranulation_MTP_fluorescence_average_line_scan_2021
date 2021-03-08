# Utility Functions
import numpy as np 
import pandas as pd 

# find middle:
def find_middle(in_column):
    """
    Find the middle index of input data column/array
    """
    middle = float(len(in_column))/2
    return int(np.floor(middle))
    # if even, pick the first value, if odd, keep middle
    #if middle % 2 != 0:
        # odd
    #    return int(np.floor(middle))
    #else:
    #    return int(middle)

# realign:
def realign_data(in_data, align = "max"):
    """
    Center data around maximum or center of shortest column, pad with 0's 
    Args:
        in_data: array of input data
        align (str): "max" or "center", max will provide shifts to align maximum of input  data, whereas "center" will shift to middle index.
    
    Returns:
        d - new dataframe with realigned data
        shifts - how each entry was shifted
    """
    x, y = in_data.shape
    d = pd.DataFrame(0, index=np.arange(x), columns = np.arange(y))
    shifts = np.zeros(y)
    
    # Find longest length sample and find it's peak/midpoint
    ind_longest = np.argmin((in_data == 0).astype(int).sum(axis=0).values)
    peak_longest = np.argmax(in_data.loc[:, ind_longest].values)
    mid_longest = find_middle(in_data.index[in_data[ind_longest]!=0].values)
    
    # arrange the rest of the data's peaks into the new dataframe lining up to longest peak or longest midpoint
    for column in in_data:
        if align == "max":
            peak = np.argmax(in_data[column].values)
            pdiff = peak_longest - peak
            d[column] = in_data[column].shift(periods=pdiff, fill_value=0)
            # check shifted max location of input is same as reference peak
            assert np.argmax(d[column]) == peak_longest
            shifts[column] = pdiff
        elif align == "center":
            mid = find_middle(in_data.index[in_data[column]!=0].values)
            pdiff = mid_longest - mid
            d[column] = in_data[column].shift(periods=pdiff, fill_value=0)
            assert find_middle(d[column].values) == mid_longest
            shifts[column] = pdiff
            
    return d, shifts