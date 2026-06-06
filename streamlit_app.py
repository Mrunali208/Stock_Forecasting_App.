import streamlit as st
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
from pmdarima import auto_arima

def download_data(symbol, start, end):
    df = yf.download(symbol, start=start, end=end)
    return df

st.title('Stock Price Prediction with ARIMA')

stock_symbol = st.sidebar.text_input('Enter Stock Symbol (e.g., AAPL):', 'AAPL')
start_date = st.sidebar.date_input('Start Date:', pd.to_datetime('2018-01-01'))
end_date = st.sidebar.date_input('End Date:', pd.to_datetime('2024-12-31'))
forecast_steps = st.sidebar.slider('Forecast Days:', 1, 90, 30)

if st.sidebar.button('Run Prediction'):
    if stock_symbol and start_date and end_date:
        with st.spinner('Downloading data and training model...'):
            df = download_data(stock_symbol, start_date, end_date)
            if df.empty:
                st.error(f"Could not download data for {stock_symbol}. Please check the symbol and date range.")
            else:
                st.subheader(f"Historical Data for {stock_symbol}")
                st.write(df.head())

                close_series = df['Close'].copy() if 'Close' in df.columns else df[('Close', stock_symbol)].copy()
                close_series = close_series.fillna(method='ffill')

                st.subheader("ARIMA Model Training")
                with st.spinner('Finding optimal ARIMA order...'):
                    # Auto ARIMA will try multiple (p, d, q) combinations and pick the best one
                    model_auto = auto_arima(close_series,
                                            start_p=1, start_q=1,
                                            max_p=5, max_q=5,
                                            seasonal=False,
                                            d=1,
                                            trace=False, # Set to False for cleaner output in Streamlit
                                            error_action='ignore',
                                            suppress_warnings=True,
                                            stepwise=True)
                    st.write(f"Optimal ARIMA order: {model_auto.order}")

                with st.spinner('Fitting ARIMA model...'):
                    model = ARIMA(close_series, order=model_auto.order)
                    fitted_model = model.fit()
                    st.write("Model fitting complete.")
                st.subheader(f"Forecast for {stock_symbol} (Next {forecast_steps} Days)")
                forecast = fitted_model.forecast(steps=forecast_steps)

                forecast_index = pd.date_range(start=close_series.index[-1] + pd.Timedelta(days=1), periods=forecast_steps)

                fig, ax = plt.subplots(figsize=(14, 6))
                ax.plot(close_series, label='Historical')
                ax.plot(forecast_index, forecast, label='Forecast', color='green')
                ax.set_title(f"{stock_symbol} ARIMA Forecast (Next {forecast_steps} Days)")
                ax.set_xlabel("Date")
                ax.set_ylabel("Closing Price (USD)")
                ax.legend()
                ax.grid(True)
                plt.tight_layout()

                st.pyplot(fig)

                st.success('Prediction complete!')
    else:
        st.warning('Please enter a stock symbol and select valid dates.') 

df.plot(close_series, )