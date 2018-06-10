
from datetime import datetime
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
    return datetime.strptime(t, '%Y %m %d %H')
