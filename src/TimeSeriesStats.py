#Import libraries
import numpy as np

#Metrics to evaluate time series forecasts
def model_performance(predictions, actual, model_name, return_metrics = True):
    errors = predictions - actual
    mape = np.mean(np.abs(errors)/np.abs(actual)) * 100
    mse = np.square(errors).mean()
    rmse = np.sqrt(mse)
    mae = np.abs(errors).mean()
    metrics = {'MAE': mae,'MAPE':mape,'MSE': mse, 'RMSE':rmse}
    print(model_name,'Performance Metrics')
    print('=======================================')
    print('MAE:{}\nMAPE:{}%\nMSE:{}\nRMSE:{}'.format(metrics['MAE'],metrics['MAPE'],metrics['MSE'],metrics['RMSE']))
    if return_metrics == True:
        return(metrics)
        
    
