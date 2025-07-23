# 📈 Stock Price Forecasting App

An advanced Stock Price Forecasting System built with Streamlit that leverages multiple time series models including ARIMA, SARIMA, Prophet, and LSTM to predict future stock prices.

---

## 📌 Features

✅ Interactive Streamlit web interface  
✅ Load stock data from CSV or yfinance  
✅ Support for multiple forecasting models:
- ARIMA
- SARIMA
- Prophet
- LSTM  
✅ Auto train & visualize forecasts  
✅ ACF/PACF and trend analysis  
✅ Downloadable outputs (planned)  
✅ Plotly-powered interactive visualizations

---

## 🧠 Models Included

| Model   | Type        | Use Case                    |
|---------|-------------|-----------------------------|
| ARIMA   | Statistical | Simple, linear patterns     |
| SARIMA  | Statistical | Seasonal patterns           |
| Prophet | Hybrid      | Trend + seasonality + outliers |
| LSTM    | Deep Learning | Complex, nonlinear sequences |

---

## 📂 Project Structure
Stock_Forecasting_App/
│
├── streamlit_app.py # Streamlit frontend
├── TIME_SERIES_AND_STOCK_ANALYSIS_pyib.ipynb # Model training notebook
├── DOCUMENTATION.md # Detailed documentation
├── README.md
├── requirements.txt

📚 Tech Stack
Frontend: Streamlit
Backend / Forecasting: Python (statsmodels, fbprophet, keras)
Data Handling: Pandas, NumPy
Visualization: Matplotlib, Plotly
Time Series: statsmodels, Prophet, TensorFlow/Keras

🛠️ Future Enhancements
✅ Dynamic stock ticker selection (in progress)
⏳ Downloadable forecast reports
🔐 Secure user authentication
📅 Scheduling model retraining

