#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#!/usr/bin/env python
# coding: utf-8

# In[ ]:

import pandas as pd
import numbers
import numpy as np
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style='darkgrid')
import geopandas as gpd

plt.rcParams.update({
    # 'font.sans-serif': 'Comic Sans MS',
    #'font.family': 'serif'
})

def Performance_metrics(X, Y, YesorNo):
    X = np.array(X).reshape(-1,)
    Y = np.array(Y).reshape(-1,)
    r2 = np.corrcoef(X, Y)[0, 1]**2
    pbias = 100 * np.sum((X - Y)) / np.sum(X)
    nse = 1 - np.sum((X - Y)**2) / np.sum((X - np.mean(X))**2)
    rmse = np.sqrt(np.mean(np.square(X - Y)))
    r = np.corrcoef(X, Y)[0, 1]
    s = np.std(Y) / np.std(X)
    b = np.mean(Y) / np.mean(X)
    kge = 1 - np.sqrt((r - 1)**2 + (s - 1)**2 + (b - 1)**2)
    if YesorNo == "Yes":
        return format(r2, ".3f"), format(nse, ".3f"), format(kge, ".3f"), format(pbias, ".3f"), format(rmse, ".3f")
    elif YesorNo == "No":
        print(f'R\N{SUPERSCRIPT TWO}: {r2:.3f}, NSE: {nse:.3f}, KGE: {kge:.3f}, PBias%: {pbias:.3f}, RMSE: {rmse:.3f}')

def Scatter_Violin_Plots(X, Y, Xlable1, Ylable1, Ylable2, title, fc):
    X = np.array(X).reshape(-1,)
    Y = np.array(Y).reshape(-1,)
    max_value = np.array((X, Y)).max()
    min_value = np.array((X, Y)).min()
    
    fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(8, 4.5), constrained_layout= True)
    
    ax1.scatter(X, Y, color=f'{fc}', edgecolor='k', alpha=0.7, s=60)
    ax1.set_yscale('log')
    ax1.set_xscale('log')
    ax1.plot([0.5*min_value, 1.8*max_value], [0.5*min_value, 1.8*max_value], '--', color='#C9494D', linewidth=2.5, alpha=0.9)
    ax1.set_xlabel(f'{Xlable1}', fontsize=16)
    ax1.tick_params(axis='x', labelsize=14)
    ax1.set_ylabel(f'{Ylable1}', fontsize=16)
    ax1.tick_params(axis='y', labelsize=14)
    ax1.grid(True)
    #ax1.set_xlim(0.5*min_value, 1.8*max_value)
    #ax1.set_ylim(0.5*min_value, 1.8*max_value)
    ax1.set_facecolor("#FAFAFA")   
    ax1.set_title('Scatter Plot', size=18)
    ax1.tick_params(labelsize=12)
    
    data_train = pd.DataFrame({f'{Xlable1}':X, f'{Ylable1}':Y})
    data_train = data_train.melt()
    data_train.rename(columns = {'value':'counts'}, inplace = True)
    data_train[' '] = ' '
    
    sns.violinplot(data = data_train, y= 'counts', split=True, hue='variable',  x=' ', palette=f'light:{fc}', ax=ax2, inner="quart",  gap=.04, density_norm="count")
    ax2.set_facecolor("#FAFAFA")  
    ax2.set_ylabel(f'{Ylable2}', fontsize=16)
    ax2.grid(True)
    ax2.set_title('Violin Plot', size=18)
    ax2.tick_params(labelsize=12) 
    ax2.legend(title=False, facecolor = "w", fontsize=14, loc='lower center', bbox_to_anchor=(0.5, -0.22), ncol=2 , columnspacing=0.8, handletextpad=0.3, handlelength=0.8)
    fig.suptitle(f'{title}', size=18, x= 0.5)

    plt.show()

def Hbar(A, Title, fc):
    fig, axs = plt.subplots(1, 1, figsize=(8, 6), constrained_layout=True)
    A.plot.barh( color=f'{fc}', edgecolor='k', alpha=0.8,  width = 0.8) 
    axs.set_title(f'{Title}', size=18)
    axs.set_ylabel("Features", size= 16)
    axs.set_xlabel("Importance (%)", size= 16)
    axs.tick_params(labelsize=14)
    axs.set_facecolor("#F0F0F0")
    axs.set_xlim([0, 100])
    axs.bar_label(axs.containers[0], label_type='edge', size=11, padding=3)
    axs.yaxis.grid(False)
    axs.xaxis.grid(True)
    plt.show()