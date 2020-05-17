#Import libraries
import numpy as np

#Metrics to evaluate time series forecasts
def model_performance(predictions, actual):
    errors = predictions - actual
    mape = np.mean(np.abs(errors)/np.abs(actual))
    mse = np.square(errors).mean()
    rmse = np.sqrt(mse)
    mae = np.abs(errors).mean()
    metrics = {'MAE': mae,'MAPE':mape,'MSE': mse, 'RMSE':rmse}
    return(metrics)