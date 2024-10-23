# Time Series Analysis on HPG Stock Data

## Overview
This project focuses on time series analysis using the stock data of Hòa Phát Group (HPG) from 2010 to 2024. The analysis includes decomposing the data, stationarity checks, and forecasting using ARIMA models. We also explore different data splitting techniques such as Expanding and Sliding Window to evaluate model performance.

## Files

- **Timeseries.pdf**: This document outlines the detailed requirements for the analysis, including the tasks and objectives related to time series forecasting of HPG stock prices.
- **HPG_2010_2024.xlsx**: The dataset contains stock price data of Hòa Phát Group from 2010 to 2024.
- **TimeSeriesStock.ipynb**: Jupyter notebook containing the full implementation of the time series analysis, including:
  - Data preprocessing
  - Stationarity checks using ADF test
  - ARIMA model fitting
  - Data splitting using Expanding and Sliding Window techniques
  - Model evaluation and forecasting future stock prices

## Requirements
- Python 3.x
- Libraries:
  - `pandas`
  - `numpy`
  - `statsmodels`
  - `matplotlib`
  - `sklearn`

You can install the required libraries using the following command:
```bash
pip install pandas numpy statsmodels matplotlib scikit-learn
  
