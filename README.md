# 📈 Time Series Analysis on HPG Stock Data

![HPG Logo](https://upload.wikimedia.org/wikipedia/vi/thumb/7/77/HPG_H%C3%B2a_Ph%C3%A1t_Group.png/220px-HPG_H%C3%B2a_Ph%C3%A1t_Group.png)

## 🌟 Overview
This project focuses on **time series analysis** using the stock data of **Hòa Phát Group (HPG)** from **2010 to 2024**. The analysis involves:
- Decomposing the stock price data
- Checking for stationarity and correlations
- Forecasting future prices using ARIMA models
- Exploring data splitting techniques: **Expanding Window** and **Sliding Window**

## 📂 Files Included

| File Name                 | Description                                                                          |
|---------------------------|--------------------------------------------------------------------------------------|
| **Timeseries.pdf**         | A document outlining tasks and objectives for time series analysis on HPG stock data.|
| **HPG_2010_2024.xlsx**     | The dataset containing HPG stock price data from 2010 to 2024.                       |
| **TimeSeriesStock.ipynb**  | Jupyter notebook with the complete implementation of the time series analysis.       |

## ⚙️ Installation

To set up the environment, install the required Python libraries by running:

```bash
pip install pandas numpy statsmodels matplotlib scikit-learn
```
## 🛠️ Tasks Performed
1. Data Decomposition:
- The stock price data was decomposed into trend, seasonal, and residual components for better analysis.
2. Stationarity Check:
- The Augmented Dickey-Fuller (ADF) test was applied to check the stationarity of the data.
3. ARIMA Model:
- Fitted an ARIMA model on 80% of the data for training, followed by model evaluation and forecasting.
4. Expanding and Sliding Window Techniques:
- Compared the model performance using both Expanding Window and Sliding Window techniques.
5. Forecasting:
- Predicted future stock prices using the trained ARIMA model.
  
## 📊 Visualizations
We have provided several visualizations in the notebook, including:
- Time series decomposition plots.
- ADF test results.
- Forecast vs. actual stock prices.
- Model performance comparisons for Expanding and Sliding Window splits.
## 🔍 How to Run
1. Clone the repository to your local machine:
```bash
git clone https://github.com/yourusername/HPG-Stock-TimeSeries-Analysis.git
```
2. Open the Jupyter notebook TimeSeriesStock.ipynb.
3. Ensure the dataset HPG_2010_2024.xlsx is in the same directory as the notebook.
4. Run the notebook cells to execute the analysis.
## 🚀 Future Work
- Implement advanced models like SARIMA or Prophet for improved forecasting.
- Incorporate additional market indicators such as Volume or Volatility for enhanced predictions.
- Expand the dataset to include multiple companies for broader financial analysis.
## 👨‍💻 Author
Dat Nguyen  <br>
Email: ngvdat.w@gmail.com  <br>
GitHub: github.com/vdat-18  <br>
