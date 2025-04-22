# Air Pollution Data Analysis

This repository contains a Python script (`main.py`) that performs exploratory data analysis on an air pollution dataset (`Python_Dataset.csv`). The script utilizes libraries such as pandas for data manipulation, matplotlib and seaborn for static visualizations, and plotly for interactive geographical plots.

## Overview

The script reads the air pollution dataset, cleans it by removing rows with missing pollutant values, and generates the following visualizations to understand the data:

1.  **Line Plot - Pollution Trend for One State:** Shows the trend of the average pollutant level over time for the state with the most entries in the dataset.
2.  **Bar Chart - Avg Pollution Per State (Top 10):** Displays the top 10 states with the highest average pollution levels.
3.  **Histogram - Pollutant Average Distribution:** Illustrates the distribution of the average pollutant values across the entire dataset.
4.  **Pie Chart - Pollutant ID Distribution:** Shows the proportion of each unique pollutant ID present in the dataset.
5.  **Scatter Plot - Geo Location by Pollution (State-wise):** Generates interactive scatter plots for each state, visualizing the pollution level (color-coded) at different geographical locations (longitude and latitude). Hovering over the points reveals the city and pollutant ID.
6.  **Box Plot - Pollution Spread by Pollutant (State-wise):** Presents box plots showing the distribution of average pollution levels for each pollutant type within each state.
7.  **Heatmap - Correlation (Overall):** Displays a heatmap showing the correlation coefficients between the minimum, maximum, and average pollutant values.
8.  **Pair Plot (Overall):** Creates a matrix of scatter plots showing the pairwise relationships between the minimum, maximum, and average pollutant values, along with their individual distributions.

## Setup

To run the script, you need to have the following Python libraries installed:

-   pandas
-   matplotlib
-   seaborn
-   plotly

You can install these libraries using pip:
