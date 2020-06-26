#Function plots time series data
def timeseries_plot(series, figsize = None , title = None, xlabel = None, ylabel = None,
                    title_dict = None, label_dict = None,color = None,ax=None, alpha = None,
                   fontsize=None, fontweight = None, style = None):
    """
    Plot Time Series Data
    """
    plot = series.plot(color = color,alpha=alpha, ax=ax)
    plot.set_title(title, fontdict=title_dict,fontsize=fontsize, fontweight = fontweight, 
                   style = style)
    plot.set_ylabel(ylabel,fontdict=label_dict,fontsize=fontsize, fontweight = fontweight, 
                    style = style)
    plot.set_xlabel(xlabel,fontdict=label_dict,fontsize=fontsize, fontweight = fontweight, 
                    style = style)
    return plot