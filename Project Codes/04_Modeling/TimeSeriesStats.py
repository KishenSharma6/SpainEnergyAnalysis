#Import libraries
import numpy as np

#Metrics to evaluate time series forecasts
def model_performance(predictions, actual):
    errors = predictions - actual
    mse = np.square(errors).mean()
    rmse = np.sqrt(mse)
    mae = np.abs(errors).mean()
    print "METRICS\nMSE:{}\nRMSE:{}\nMAE:{}".format(mse,rmse,mae)