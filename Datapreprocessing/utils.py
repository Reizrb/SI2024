import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
from matplotlib.lines import Line2D

def Map_T1(df_final, train_set, test_set, State_poly, ZC_US_poly, State_Abb, fc, model_name):
    fig, ax = plt.subplots(figsize=(15, 15))
    State_poly.plot(ax=ax, facecolor='white', edgecolor='black', linewidth=0.8, label='State border')
    ZC_US_poly.plot(ax=ax, facecolor='white', edgecolor='black', linewidth=0.05, label='Zip code border')
    train_set.plot(ax=ax, color=fc[0], edgecolor='black', linewidth=0.6, label='Training', alpha=0.85)
    test_set.plot(ax=ax, color=fc[1], edgecolor='black', linewidth=0.6, label='Trsting', alpha=0.85)
    State_poly.boundary.plot(ax=ax, edgecolor='black', linewidth=0.8, label='State border')
    State_Abb_filtered = State_Abb[State_Abb['STATE'].isin(['TX', 'LA'])]
    for lon, lat, state in zip(State_Abb_filtered['LON'], State_Abb_filtered['LAT'], State_Abb_filtered['STATE']):
        if lon < df_final.total_bounds[0] - 0.25 or lon > df_final.total_bounds[2] + 0.25:
            lon = float(input(f"The defined centroid longitute of {state} is out of figure boarder! Enter a longitute ranging from {(df_final.total_bounds[0] - 0.25):.2f} to {(df_final.total_bounds[2] + 0.25):.2f} for this state: "))
            ax.text(lon, lat, state, fontsize=21, ha='center', va='center')
        if lat < df_final.total_bounds[1] - 0.25 or lat > df_final.total_bounds[3] + 0.25:
            lat = float(input(f"The defined centroid latitute of {state} is out of figure boarder! Enter a latitute ranging from {(df_final.total_bounds[1] - 0.25):.2f} to {(df_final.total_bounds[3] + 0.25):.2f} for this state: "))
            ax.text(lon, lat, state, fontsize=21, ha='center', va='center')
        else:
            ax.text(lon, lat, state, fontsize=21, ha='center', va='center')  
    legend_handles = [Patch(facecolor=fc[0], edgecolor='black', label='Training (299)', alpha=0.85), Patch(facecolor=fc[1], edgecolor='black', label='Testing (100)', alpha=0.85), Line2D([0], [0], color='black', lw=2, label='State border'), Line2D([0], [0], color='black', lw=0.5, label='CONUS Zip codes')]
    ax.legend(handles=legend_handles, loc = 'lower right', fontsize=15,facecolor='white')
    ax.set_xlim(df_final.total_bounds[0] - 0.25, df_final.total_bounds[2] + 0.25)
    ax.set_ylim(df_final.total_bounds[1] - 0.25, df_final.total_bounds[3] + 0.25)
    ax.arrow(df_final.total_bounds[2] - 0.2, df_final.total_bounds[3] - 0.25, 0, 0.1,width=0, head_width=0.5, head_length=0.4, fc='black', ec='black', length_includes_head=True, overhang=0.3, zorder=10)
    ax.text(df_final.total_bounds[2] - 0.2, df_final.total_bounds[3] - 0.08, 'N', fontsize=16, ha='center')
    ax.tick_params(labelsize=16)
    ax.set_facecolor("#F0F0F0")
    for spine in ax.spines.values():
        spine.set_edgecolor('black')
    plt.grid(False)
    plt.show()
