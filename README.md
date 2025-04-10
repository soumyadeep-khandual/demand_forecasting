# DEMAND FORECASTING EDA

## Data Preparation and Cleaning for Time Series

### Handling Missing Values
Handling missing values is a critical step in the preprocessing of time series data, as incomplete data can lead to biased estimates, reduce the statistical power of analyses, and ultimately result in less reliable conclusions. The nature of time series data often adds complexity to handling missingness because the temporal ordering and potential autocorrelation between observations need to be considered. 

#### IMPUTATION BASED
replacing missing data with substituted values
based on other available data

`-` these methods can distort the time series' characteristics, particularly if the data exhibits strong seasonality or trend components.

- **Mean/Median Imputation:** Replacing missing values with
the mean or median of the non-missing points 
    - `+` simple
    - `-` does not account for temporal dependencies.
    - `-` not suitable for longer gaps.
- **Last Observation Carried Forward (LOCF):** Filling missing values with the last observed value.
    
    - `+` reasonable for data with minor gaps.
    - `-` not suitable for longer gaps.

- **Linear Interpolation:** Estimating missing values using linear interpolation between observed data points.
    - `+` can work for longer gaps.
    - `+` simple and suitable if change between successive points is linear in nature.
    - `-` wont work if there is a non linear / complex relationship among successive points.

- **Seasonal Adjustment:** When the data exhibits strong seasonality, missing values can be imputed based on seasonal patterns. For instance, missing monthly sales data could be imputed using the same month's data from previous years.
    - `+` good for data with strong seasonal effects.
    - `-` may not account for trends in data.

#### MODEL BASED
Model-based methods use statistical models to estimate missing values, taking into account the autocorrelation structure of the time series.

- **Time Series Decomposition:** Decomposing the series into trend, seasonal, and residual components, and then imputing missing values in each component separately, often using interpolation.
    - `+` works with longer gaps
    - `-` may lead to bias in models.

- **State Space Models and Kalman Filtering:**
These approaches model the time series as a linear dynamic system and are particularly effective for imputing missing values in data with complex temporal structures. `[NOT COMPLETE]`

- **ARIMA Models:** Autoregressive Integrated Moving Average (ARIMA) model can also be used to predict missing values based on the observed values before and after the missing point.
    - `+-` same as TS Decomposition

#### MULTIPLE IMPUTATION
#### DROPPING MISSSING DATA
In some cases, especially when the proportion of missing data is very small or if the missing data is considered Missing Completely at Random, it might be reasonable to simply exclude the missing observations from the analysis. However, this method can lead to a loss of valuable information and reduce the sample size, potentially biasing
the results.

### Data Transformation and Normalization
Data transformation involves applying a mathematical modification to
each data point in a dataset to change the shape of its distribution. The
goal is to achieve a more linear relationship between variables, reduce
skewness, stabilize the variance across the series.
#### Data Transformation
- **Log Transformation:** 
    + Useful for data with exponential growth
patterns or multiplicative errors, 
    + the log transformation can
help stabilize variance and make the data more symmetric.

- **Square Root Transformation:** 
    + Applied to reduce right skewness, it's milder than a log transformation and can be used for count data.
- **Box-Cox Transformation:** A more generalized transformation that 
    + can handle positive, zero, and negative values,
    + automatically determines the best power transformation to make the data more normal-like.
- **Differencing:** differencing involves subtracting the current value from the previous value, thereby focusing on the changes between consecutive observations. 
    + can help in removing trends and seasonality, making the series more stationary.

#### Normalization
involves rescaling the data to a specific range, often [0, 1] or [-1, 1], without distorting differences in the ranges of values or losing information. 

`+` important when comparing or combining data measured on different scales, 
    
`+` when using machine learning algorithms that assume data is on a similar scale.

- **Min-Max Scaling:** This method subtracts the minimum value of the feature and then divides by the range of the feature. As a result, the distribution is now within the range [0, 1].
- **Z-score Normalization (Standardization):** This method involves subtracting the mean of the feature and then dividing by the standard deviation, resulting in data centered around 0 with a standard deviation of 1. 
    + This is useful when you want to compare the relative standing of values within a feature.

## Exploratory Data Analysis (EDA) for Time Series
Visualizing Time Series Data provides intuitive insights into the underlying patterns, trends, seasonality, and anomalies within the data.
- **Line Plots:**
    + The most basic to visualize time series data. 
    + gives ntuition about trends over time, seasonality, and any outliers or unusual deviations in the series.
- **Seasonal Decomposition Plots**
Seasonal decomposition plots break down the time series into its trend, seasonal, and residual components, typically resulting from time series decomposition methods like STL.
    + visually assess the strength and nature of the trend and seasonal patterns, as well as the randomness of the residual.
- **Autocorrelation Function (ACF)
and Partial Autocorrelation
Function (PACF) Plots**
    + The ACF plot displays the correlation of the series with its lags, 
    + PACF plot shows the partial correlation of the series with its lags, controlling for the values of the intermediate lags.
    + These plots are instrumental in identifying the order of autoregressive (AR) and moving average (MA) components for ARIMA modeling.

- **Heat Maps**
useful for visualizing time series data that
spans over long periods, allowing analysts to detect patterns, cycles, and
anomalies. Time can be represented on one axis (e.g., years along the y-
axis), with the time unit's subdivisions (e.g., months) on the other axis,
and colors indicating the magnitude of the variable of interest.
    + effective in highlighting seasonal patterns and anomalies
within the data.

- **Box  Plots**
used to examine the distribution of the time series data across different time intervals (e.g., months or quarters). This visualization technique is useful for 
    + identifying seasonal effects, outliers, and changes in the variability of the series over time.

## Descriptive Statistics in Time Series
`TODO`
- Central Tendency and Dispersion
- Trends and Seasonality
- Autocorrelation
- Stationarity
- Skewness and Kurtosis

## Identifying Patterns
Patterns in time series data are often categorized into three main types:
trend, seasonality, and cyclic patterns.
- **Trend** represents a long-term increase or decrease in the data. It indicates the overall direction in which the series is moving over time. Identifying trends is crucial for forecasting and
understanding the underlying momentum of the series.
- **Seasonality** refers to patterns that repeat at regular intervals, such as daily, weekly, monthly, or quarterly. Seasonality is often influenced by external factors like weather, holidays, or business cycles and is critical for planning and decision-making in various fields, including retail, finance, and agriculture.
- **Cyclic** patterns differ from seasonal patterns in that they do not have a fixed period. Instead, they are influenced by business or economic cycles and can vary in duration. Identifying these cycles helps in understanding the broader economic and market forces at play.

## Identifying Anomalies
Anomalies, or outliers, are data points that deviate significantly from the pattern expected based on the rest of the data. Anomalies can be of particular interest because they may indicate significant but unexpected events, such as system failures, economic shocks, or sudden market movements.
- **Point Anomalies:** 
    + single data point significantly deviates from the rest of the data. 
    + can often be attributed to specific, identifiable events.

- **Contextual Anomalies:** are data points that are anomalous in a specific context. For example, a low temperature might be normal in winter but would be considered anomalous in summer.

- **Collective Anomalies:** involve a collection of data points that deviate from the overall pattern when considered together, even though the individual data points may not be anomalous by themselves. This can often be seen in time series with sudden shifts in variance or mean. 
## REFERENCES
- https://cran.r-project.org/web/packages/imputeTS/readme/README.html
- Time Series Data Analysis Unlocking Patterns and Predictions in Sequential Data By Brian Paul.