#Import libraries
import numpy as np

#Metrics to evaluate time series forecasts
def model_performance(predictions, actual):
    errors = predictions - actual
    mse = np.square(errors).mean()
    rmse = np.sqrt(mse)
    mae = np.abs(errors).mean()
    metrics = {'MSE': mse, 'RMSE':rmse, 'MAE': mae}
    return(metrics)