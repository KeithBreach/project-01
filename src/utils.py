
from datetime import datetime
from sklearn.preprocessing import MinMaxScaler
import pandas as pd

def get_temporal_data(zipcode, df):
    
    zip_temporal_df = df.loc[df["Zip Code"] == zipcode, :]
    # trend_df = pd.DataFrame()
    return zip_temporal_df


def get_spatial_data(year, df):
    
    year_spatial_df = df.loc[df["Year"] == year, :]
    # trend_df = pd.DataFrame()
    return year_spatial_df


def parse_time(t):
    """
    :param t:
    :return:
    """
    return datetime.strptime(t, '%Y %m %d %H')


# create a differenced series
def create_difference_sequence(sequence, interval=1):
    """Create difference sequence given input 'sequence' and 'interval'.

    :param sequence:
    :param interval:
    :return:
    """

    diff = list()
    for i in range(interval, len(sequence)):
        value = sequence[i] - sequence[i - interval]
        diff.append(value)
    return pd.Series(diff)


def rescale(x, scale_range=(0,1)):
    scaler = MinMaxScaler(feature_range=scale_range)
    return scaler(x), scaler