import yfinance as yf
from pathlib import Path
from datetime import date
from prophet import Prophet
import joblib

TODAY = date.today()

TODAY = date.today()
BASE_DIR = Path(__file__).resolve(strict=True).parent
ticker = "MSFT"


def train(ticker: str = "MSFT") -> None:
    data = yf.download(
        tickers=ticker, start="2020-01-01", end=TODAY.strftime("%Y-%m-%d")
    )
    data.head()

    df_forecast = data.copy()
    print()
    # data["Adj Close"].plot(title=f"{ticker} Stock Adjusted Closing Price")

    df_forecast = data.copy()
    df_forecast.reset_index(inplace=True)
    df_forecast["ds"] = df_forecast["Date"]
    df_forecast["y"] = df_forecast["Adj Close"]
    df_forecast = df_forecast[["ds", "y"]]
    df_forecast

    model = Prophet()
    model.fit(df_forecast)
    joblib.dump(model, Path(BASE_DIR).joinpath(f"{ticker}.joblib"))
