import pandas as pd

def update_timestamp(series):
    series = series.apply(lambda x: x[0:10])
    series = series.apply(lambda x: str(x[8:10]) + '/' + str(x[5:7]) + '/' + str(x[0:4]))

    return series

