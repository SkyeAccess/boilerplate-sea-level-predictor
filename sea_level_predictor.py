import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], label='Data')

    # Create first line of best fit
    slope, intercept, _, _, _ = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    years_all = np.arange(df['Year'].iloc[0], 2051)
    line_all_data = slope * years_all + intercept
    plt.plot(years_all, line_all_data, color='red', label='Best Fit Line (All Data)')

    # Create second line of best fit
    recent_years_df = df[df['Year'] >= 2000]
    slope_recent, intercept_recent, _, _, _ = linregress(recent_years_df['Year'], recent_years_df['CSIRO Adjusted Sea Level'])
    years_recent = np.arange(2000, 2051)
    line_since_2000 = slope_recent * years_recent + intercept_recent
    plt.plot(years_recent, line_since_2000, color='green', label='Best Fit Line (Since 2000)')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
