import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def scatter_plot(df, n_col = 3, outcome_col = None, f_size = (15,15)):
    
    '''
    Function to generate scatter plots,
    Inputs:
    df: pandas dataframe of features to plot
    n_col: number of columns
    outcome_col: string specifying the outcome column. If None, will not group
    n_bins: number of bins
    plot_legend: Boolean. should a legend be included in the plot?
    f_size: tuple of (x size, y size) to specify size of plot
    '''

    if outcome_col is None:
        raise ValueError
    else:
        n_features = df.shape[1] -1
        feature_names = [x for x in df.columns.values if x != outcome_col]
        df_features = df.loc[:, feature_names]

    if n_features % n_col == 0:
        n_row = n_features // n_col
    else:
        n_row = n_features // n_col + 1
        
    outcome_data = df.loc[:, outcome_col]


    f, axarr = plt.subplots(n_row, n_col, figsize = f_size, dpi=80)
    
    v = 0
    for i in np.arange(n_row):
        for j in np.arange(n_col):
            

        # turn off axis if empty grids
            if v >= n_features:
                if n_row == 1:
                    axarr[j].axis('off')
                    continue
                elif n_col == 1:
                    axarr[i].axis('off')
                    continue
                else:
                    axarr[i][j].axis('off')
                    continue
                    
            plt_data = df_features.loc[:, feature_names[v]]
            lab = feature_names[v]

            xmin = df_features.loc[:, feature_names[v]].min()
            xmax = df_features.loc[:, feature_names[v]].max()
            xnew = np.linspace(xmin, xmax ,300) 


            if (n_row == 1) and (n_col == 1):
                axarr.spines['right'].set_visible(False)
                axarr.spines['top'].set_visible(False)
                axarr.tick_params(axis=u'both', which=u'both',length=5)
            elif n_row == 1:
                axarr[j].spines['right'].set_visible(False)
                axarr[j].spines['top'].set_visible(False)
                axarr[j].tick_params(axis=u'both', which=u'both',length=5)
            elif n_col == 1:
                axarr[i].spines['right'].set_visible(False)
                axarr[i].spines['top'].set_visible(False)
                axarr[i].tick_params(axis=u'both', which=u'both',length=5)
            else:
                axarr[i][j].spines['right'].set_visible(False)
                axarr[i][j].spines['top'].set_visible(False)
                axarr[i][j].tick_params(axis=u'both', which=u'both',length=5)

            if (n_row == 1) and (n_col ==1):
                axarr.scatter(plt_data, outcome_data, label = lab, alpha = 0.6)
                axarr.set_xlabel(feature_names[v])
                axarr.set_ylabel(outcome_col)
                
            elif n_row == 1:
                axarr[j].scatter(plt_data, outcome_data, label = lab, alpha = 0.6)
                axarr[j].set_xlabel(feature_names[v])
                if j == 0:
                    axarr[j].set_ylabel(outcome_col)
                
            elif n_col == 1:
                axarr[i].scatter(plt_data, outcome_data, label = lab, alpha = 0.6)
                axarr[i].set_xlabel(feature_names[v])
                if i == 0:
                    axarr[i].set_ylabel(outcome_col)
               
            else:
                axarr[i][j].scatter(plt_data, outcome_data, label = lab, alpha = 0.6)
                axarr[i][j].set_xlabel(feature_names[v])
                if j == 0:
                    axarr[i][j].set_ylabel(outcome_col)
                
            v += 1
            

    if n_col == 1:
        f.subplots_adjust(hspace = 1)
    else:
        f.subplots_adjust(hspace = 0.5)
    #return f
