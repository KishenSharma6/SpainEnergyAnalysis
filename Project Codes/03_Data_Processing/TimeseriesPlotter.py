#Function plots time series data
def timeseries_plot(series, figsize = None , title = None, xlabel = None, ylabel = None,legend = False,label = None,
                    title_dict = None, label_dict = None,color = None,ax=None, alpha = None):
    """
    Plot Time Series Data
    """
    plot = series.plot(color = color,label = label,alpha=alpha, ax=ax)
    plot.set_title(title, fontdict=title_dict)
    plot.set_ylabel(ylabel,fontdict=label_dict)
    plot.set_xlabel(xlabel,fontdict=label_dict)
    if legend == True:
        plot.legend(fancybox = True, shadow = True, frameon = True)
    return plot