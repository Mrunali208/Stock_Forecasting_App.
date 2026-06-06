# 📈 Stock Price Forecasting Dashboard

An end-to-end Stock Price Forecasting Application built using Streamlit and multiple time-series forecasting models including ARIMA, SARIMA, Prophet, and LSTM.

The application enables users to analyze historical stock market trends, compare forecasting models, and visualize future stock price predictions through an interactive dashboard.

---

## 🚀 Features

- Interactive Streamlit Dashboard
- Real-time stock data retrieval using Yahoo Finance
- Historical stock trend visualization
- Multiple forecasting models:
  - ARIMA
  - SARIMA
  - Prophet
  - LSTM
- Model performance comparison
- ACF/PACF analysis
- Trend and seasonality analysis
- Interactive Plotly visualizations
- Forecasting for next 30 days

---

## 🧠 Forecasting Models

| Model | Type | Purpose |
|---------|---------|---------|
| ARIMA | Statistical | Linear trend forecasting |
| SARIMA | Statistical | Seasonal trend forecasting |
| Prophet | Hybrid | Trend + seasonality modeling |
| LSTM | Deep Learning | Complex nonlinear forecasting |

---

## 📊 Tech Stack

### Programming Language
- Python

### Frontend
- Streamlit

### Data Collection
- Yahoo Finance (yfinance)

### Data Analysis
- Pandas
- NumPy

### Visualization
- Plotly
- Matplotlib

### Forecasting Libraries
- Statsmodels
- Prophet
- TensorFlow / Keras

---

## 📂 Project Structure

```text
Stock_Forecasting_App/
│
├── streamlit_app.py
├── TIME_SERIES_AND_STOCK_ANALYSIS.ipynb
├── requirements.txt
├── README.md
├── DOCUMENTATION.md
└── screenshots/
```

---

## 📸 Screenshots

### Historical Closing Price

![Historical Price](screenshots/AAPL%20Closing%20Price%20(2018-2024).png)

---

### ARIMA Forecast

![ARIMA Forecast](screenshots/AAPL%20ARIMA%20Forecast%20(next%2030%20days).png)

---

### SARIMA Forecast

![SARIMA Forecast](screenshots/AAPL%20SARIMA%20Forecast%20(next%2030%20days).png)

---

### Prophet Forecast

![Prophet Forecast](screenshots/AAPL%20PROPHET%20Forecast%20(next%2030%20days).png)

---

### LSTM Forecast

![LSTM Forecast](screenshots/AAPL%20LSTM%20Forecast%20(next%2030%20days).png)

---

### Model Comparison

![Model Comparison](screenshots/Model%20Comparison-%20Actual%20vs%20Forecast.png)

---

## 📈 Model Evaluation

Models were evaluated using:

- RMSE (Root Mean Square Error)
- MAE (Mean Absolute Error)

The comparison enables users to identify the most suitable forecasting approach for a selected stock.

---

## 🔮 Future Enhancements

- Dynamic stock ticker selection
- Multi-stock comparison
- Downloadable PDF reports
- Portfolio performance analytics
- Cloud deployment using AWS
- Automated model retraining pipeline

---

## 👩‍💻 Author

**Mrunali Patil**

Aspiring Data Analyst | Python Developer | AWS Enthusiast

🔗 LinkedIn: www.linkedin.com/in/patil-mrunali

---

⭐ If you found this project useful, consider giving it a star.
